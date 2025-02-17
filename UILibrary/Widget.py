import pygame

from .Helpers import Box

from .Grid import Alignment
from .Grid import Scale
from .Grid import Fill
from .Grid import Aspect

from .Style import Theme


class Widget:
    def __init__(self, Parent, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(10, 10), Name: str = "Widget", Style = None):
        ## Rendering Setup
        self.Position = Position
        self.AbsolutePosition = Position
        self.Size = Size
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.Surface = pygame.Surface(self.Size, pygame.SRCALPHA)
        
        ## Style Setup
        self.Name = Name
        self.State = "Idle"
        self.Style = Style
        self.Theme = Theme()
        self.Visible = True
        self._Absolute = False
        self._Transparent = True

        ## Scaling & Resizing
        self.Scaled = None
        self.Docked = None
        self.Filled = None
        self.Aspect = None

        ## Interactivity
        self.Interactive = False
        self.Hovered = False
        self.Focused = False
        self.Clicked = False
        self.Holding = False
        self.RelativeMouse = pygame.Vector2(0, 0)
        self.MouseStart = pygame.Vector2(0, 0)
        
        ## Final Setup
        self.Root = False
        self.Parent = None
        self.ZIndex = 0
        self.Children = []
        self.SetParent(Parent)
        

        self.PaddingRect = pygame.Rect(0, 0, self.Size.x, self.Size.y)
  
    def __str__(self):
        Output = f"""
        ZIndex: {self.ZIndex}
        Position: {self.Position}
        Size: {self.Size}
        """
        return Output
    
    def Absolute(self):
        self._Absolute = True

        return self

    def Generate(self):
        self.Style = self.Parent.Style
        self.Style.Apply(self)

        self.MarginRect = pygame.Rect(self.Theme.Margin.left, self.Theme.Margin.top, self.Size.x - self.Theme.Margin.width, self.Size.y - self.Theme.Margin.height)
        self.PaddingRect = pygame.Rect(self.Theme.Padding.left, self.Theme.Padding.top, self.Size.x - self.Theme.Padding.width, self.Size.y - self.Theme.Padding.height)
        for Child in self.Children:
            Child: Widget
            Child.Generate()

    def SetParent(self, Parent):
        if self.Parent != None:
            self.Parent.Children.remove(self)

        if Parent != None:
            self.Parent = Parent
            if self.Parent.Style != None:
                self.Style = Parent.Style
                self.Style.Apply(self)

                self.Generate()

            self.Surface = Parent.Surface

        if Parent == None:
            self.ZIndex = 1
        else:
            self.ZIndex = Parent.ZIndex + 1
            Parent.Children.append(self)

    def SetState(self, State):
        self.State = State

    def SetSize(self, Size):
        self.Size = Size

    def SetPosition(self, Position):
        self.Position = Position

    def GetRoot(self):
        if self.Root:
            return self
        else:
            return self.Parent.GetRoot()

    def Dock(self, Alignment: Alignment):
        Alignment.Apply(self)
        self.Docked = Alignment

        return self
    
    def Constrain(self, Aspect: Aspect):
        Aspect.Apply(self)
        self.Aspect = Aspect

        return self

    def Scale(self, Scale: Scale):
        Scale.Apply(self)
        self.Scaled = Scale

        return self
    
    def Fill(self, Fill: Fill):
        Fill.Apply(self)
        self.Filled = Fill

        return self

    def Clear(self):
        for Child in self.Children:
            del Child
        self.Children = []

    def Evaluate(self):
        ## Hover Detection
        if self._Absolute:
            self.AbsolutePosition = self.Position + self.Parent.AbsolutePosition
        else:
            self.AbsolutePosition = self.Position + self.Parent.AbsolutePosition + self.Theme.Margin.center

        PhysicalRect = pygame.Rect(self.AbsolutePosition, self.PaddingRect.size)
        MousePos = self.GetRoot().Inputs.MousePosition
        self.RelativeMouse = pygame.Vector2(MousePos) - pygame.Vector2(self.AbsolutePosition)

        pygame.draw.rect(self.Surface, pygame.Color(255, 0, 255), PhysicalRect, 1)

        if PhysicalRect.collidepoint(MousePos):
            self.Hovered = True
            self.SetState("Hover")
        else:
            self.Hovered = False
            self.SetState("Idle")
        
        ## Focus & Click Detection
        if self.Clicked:
            self.Clicked = False

        if self.GetRoot().Inputs.Mouse1:
            if self.Hovered:
                if not self.Holding:
                    self.MouseStart = pygame.Vector2(MousePos) - pygame.Vector2(self.AbsolutePosition)

                self.Focused = True
                self.Holding = True
                self.SetState("Held")
            else:

                self.Focused = False
        else:
            if self.Hovered and self.Holding:
                self.Clicked = True

            
            self.Holding = False
            if not self.Hovered:
                self.SetState("Idle")

        Box(self, self.Theme.Background)

        self.Style.Apply(self)

    def Update(self):

        if self.Scaled:
            self.Scale(self.Scaled)
        if self.Docked:
            self.Dock(self.Docked)
        if self.Filled:
            self.Fill(self.Filled)
        if self.Aspect:
            self.Constrain(self.Aspect)

        ## Update Children
        for Child in self.Children:
            Child: Widget
            #try:
            Child.Evaluate()
            Child.Update()
            #except Exception as Error:
            #    print(f"Update Failed: {Error}")

        ## Update Self
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.Size = pygame.Vector2(self.Size)

        self.MarginRect = pygame.Rect(
            0, 
            0, 
            self.Size.x - self.Theme.Margin.width - self.Theme.Margin.left, 
            self.Size.y - self.Theme.Margin.height - self.Theme.Margin.top
        )

        self.PaddingRect = pygame.Rect(
            self.MarginRect.left + self.Theme.Padding.left, 
            self.MarginRect.top + self.Theme.Padding.top, 
            self.MarginRect.width - self.Theme.Padding.width, 
            self.MarginRect.height - self.Theme.Padding.height
        )

        if self._Absolute:
            self.PaddingRect = pygame.Rect(0, 0, self.Size.x, self.Size.y)

        if self._Transparent:
            ## Shitty transparency workaround because pygame is mean
            self.Surface.set_colorkey(pygame.Color(255, 0, 255))

        if self.Visible:
            if self._Absolute:
                self.Parent.Surface.blit(self.Surface.convert_alpha(), self.Position, self.Rect)
            else:
                self.Parent.Surface.blit(self.Surface.convert_alpha(), self.Position + self.Theme.Margin.topleft)
        try:
            # recreate surface to reflect size changes (for responsive layouts)
            if self._Absolute:
                self.Surface = pygame.Surface(self.Size, pygame.SRCALPHA)
            else:
                self.Surface = pygame.Surface(self.MarginRect.size, pygame.SRCALPHA) 
        except:
            pass
    