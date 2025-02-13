import pygame

from .Utils import Box


from .Style import Theme

from .Grid import Alignment
from .Grid import Scale
from .Grid import Fill
from .Grid import Aspect



class Widget:
    def __init__(self, Parent, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(10, 10), Name: str = "Widget", Style = None):
        self.Position = Position
        self.AbsolutePosition = Position
        self.Size = Size
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.Root = False
        self.Style = Style
        self.Theme = Theme.Theme()
        self.Name = Name
        self.BG = None
        
        self.State = "Idle"

        self.Visible = True
        self.Ignore = False

        self.Scaled = None
        self.Docked = None
        self.Filled = None
        self.Aspect = None

        self.Interactive = False
        self.Hovered = False
        self.Focused = False
        self.Clicked = False
        self.Holding = False
        self.RelativeMouse = pygame.Vector2(0, 0)
        self.MouseStart = pygame.Vector2(0, 0)

        self.Selected = False

        if Parent == None:
            self.ZIndex = 1
        else:
            self.ZIndex = Parent.ZIndex + 1
            Parent.Children.append(self)
        
        self.SetParent(Parent)
        self.Surface = pygame.Surface(self.Size, pygame.SRCALPHA)
        self.Children = []
  
    def __str__(self):
        Output = f"""
        ZIndex: {self.ZIndex}
        Position: {self.Position}
        Size: {self.Size}
        """
        return Output

    def SetParent(self, Parent):
        if Parent != None:
            self.Parent = Parent
            if self.Parent.Style != None:
                self.Style = Parent.Style
                self.Style.Apply(self)

                self.MarginRect = pygame.Rect(self.Theme.Margin.left, self.Theme.Margin.top, self.Size.x - self.Theme.Margin.width, self.Size.y - self.Theme.Margin.height)
                self.PaddingRect = pygame.Rect(self.Theme.Padding.left, self.Theme.Padding.top, self.Size.x - self.Theme.Padding.width, self.Size.y - self.Theme.Padding.height)
            self.Surface = Parent.Surface

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

    def Absolute(self):
        self.Ignore = True

        return self

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
        self.AbsolutePosition = self.Position + self.Parent.AbsolutePosition + self.Theme.Margin.center

        PhysicalRect = pygame.Rect(self.AbsolutePosition, self.PaddingRect.size)
        MousePos = pygame.mouse.get_pos()
        self.RelativeMouse = pygame.Vector2(MousePos) - pygame.Vector2(self.AbsolutePosition)

        if PhysicalRect.collidepoint(MousePos):
            self.Hovered = True
            self.SetState("Hover")
        else:
            self.Hovered = False
            self.SetState("Idle")
        
        ## Focus & Click Detection
        if self.Clicked:
            self.Clicked = False

        if pygame.mouse.get_pressed()[0]:
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

        self.Style.Apply(self)
        if self.BG != None:
            Box(self, self.BG)
        else:
            Box(self, self.Theme.Background)
        #pygame.draw.rect(self.Surface, pygame.Color(255, 0, 0), PhysicalRect)
        

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

        if self.Ignore:
            self.PaddingRect = pygame.Rect(
                0,0,self.Size.x,self.Size.y
            )
        
        self.Surface.set_colorkey(pygame.Color(255, 0, 255))
        if self.Visible:
            if self.Ignore:
                self.Parent.Surface.blit(self.Surface.convert_alpha(), self.Position, self.Rect)
            else:
                self.Parent.Surface.blit(self.Surface.convert_alpha(), self.Position + self.Theme.Margin.topleft)
        try:
            # recreate surface to reflect size changes (for responsive layouts)
            if self.Ignore:
                self.Surface = pygame.Surface(self.Size, pygame.SRCALPHA)
            else:
                self.Surface = pygame.Surface(self.MarginRect.size, pygame.SRCALPHA) 
        except:
            pass
    