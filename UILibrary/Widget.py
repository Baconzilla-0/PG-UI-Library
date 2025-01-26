import pygame

from .Utils import Box

from .Style import Sheet
from .Grid import Alignment
from .Grid import Scale
from .Grid import Fill

class Widget:
    def __init__(self, Parent, Style: Sheet, Name: str = "Widget", Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(10, 10)):
        self.Position = Position
        self.Size = Size
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        
        self.Theme = None
        self.Name = Name

        self.Style = Style
        self.State = "Idle"
        self.Style.Apply(self)

        self.MarginRect = pygame.Rect(self.Theme.Margin.left, self.Theme.Margin.top, Size.x - self.Theme.Margin.width, Size.y - self.Theme.Margin.height)
        self.PaddingRect = pygame.Rect(self.Theme.Padding.left, self.Theme.Padding.top, Size.x - self.Theme.Padding.width, Size.y - self.Theme.Padding.height)

        self.Visible = True
        self.Ignore = False

        self.Scaled = None
        self.Docked = None
        self.Filled = None

        self.Hovered = False
        self.Focused = False
        self.Clicked = False
        self.Holding = False
        

        self.Selected = False

        if Parent == None:
            self.ZIndex = 1
        else:
            self.ZIndex = Parent.ZIndex + 1
            Parent.Children.append(self)
        
        self.Parent: Widget = Parent
        self.Surface = pygame.Surface(self.Size, pygame.SRCALPHA)
        self.Children = []
  
    def __str__(self):
        Output = f"""
        Parent: {self.Parent}
        ZIndex: {self.ZIndex}
        Position: {self.Position}
        Size: {self.Size}
        """

        return Output

    def SetState(self, State):
        self.State = State

    def SetSize(self, Size):
        self.Size = Size

    def SetPosition(self, Position):
        self.Position = Position

    def Absolute(self):
        self.Ignore = True

        return self

    def Dock(self, Alignment: Alignment):
        Alignment.Apply(self)
        self.Docked = Alignment

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
        PhysicalRect = pygame.Rect(self.Position + self.Parent.Position + self.Theme.Margin.topleft, self.MarginRect.size)

        if PhysicalRect.collidepoint(pygame.mouse.get_pos()):
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

        ## apply the stylesheet (TODO: rewrite styling to be more html-ish)
        self.Theme = None # reset the theme so global styles can be overwritten.
        self.Style.Apply(self)
        Box(self, self.Theme.Background)
        

    def Update(self):

        if self.Scaled:
            self.Scale(self.Scaled)
        if self.Docked:
            self.Dock(self.Docked)
        if self.Filled:
            self.Fill(self.Filled)

        ## Update Children
        for Child in self.Children:
            Child: Widget

            Child.Evaluate()
            Child.Update()

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
    