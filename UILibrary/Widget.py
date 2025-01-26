import pygame

from .Theme import Theme
from .Grid import Alignment
from .Grid import Scale
from .Grid import Fill

class Widget:
    def __init__(self, Parent, Theme: Theme = None, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(10, 10)):
        self.Position = Position
        self.Size = Size
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.ContentRect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.Padding = pygame.Rect(0, 0, 0, 0)

        self.Visible = True

        self.Scaled = None
        self.Docked = None
        self.Filled = None

        self.Hovered = False
        self.Focused = False
        self.Clicked = False
        self.Holding = False

        self.Selected = False

        self.Theme = Theme
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

    def SetSize(self, Size):
        self.Size = Size

    def SetPosition(self, Position):
        self.Position = Position

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
        PhysicalRect = pygame.Rect(self.Position + self.Parent.Position, self.Size)

        if PhysicalRect.collidepoint(pygame.mouse.get_pos()):
            self.Hovered = True
        else:
            self.Hovered = False
        
        ## Focus & Click Detection
        if self.Clicked:
            self.Clicked = False

        if pygame.mouse.get_pressed()[0]:
            if self.Hovered:
                self.Focused = True
                self.Holding = True
            else:
                self.Focused = False
        else:
            if self.Hovered and self.Holding:
                self.Clicked = True

            self.Holding = False
        

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

        Offset = pygame.Vector2(self.Padding.left / 2, self.Padding.top / 2)
        Position = self.Position + Offset
        Size = pygame.Rect(pygame.Vector2(0, 0), self.Size - pygame.Vector2(self.Padding.right / 2, self.Padding.bottom / 2))
        self.ContentRect = Size

        self.Surface.set_colorkey(pygame.Color(255, 0, 255))
        if self.Visible:
            self.Parent.Surface.blit(self.Surface.convert_alpha(), Position, Size)
        try:
            self.Surface = pygame.Surface(Size.size, pygame.SRCALPHA) # recreate surface to reflect size changes (for responsive layouts)
        except:
            pass
    