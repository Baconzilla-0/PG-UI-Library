import pygame

from .Theme import Theme
from .Grid import Alignment
from .Grid import Scale

class Widget:
    def __init__(self, Parent, Theme: Theme, Position: pygame.Vector2, Size: pygame.Vector2):
        self.Position = Position
        self.Size = Size
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.Padding = pygame.Rect(0, 0, 0, 0)

        self.Scaled = None
        self.Docked = None

        self.Hovered = False
        self.Focused = False
        self.Clicked = False
        self.Holding = False

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

    def Dock(self, Alignment: Alignment):
        Alignment.Apply(self)
        self.Docked = Alignment

        return self
    
    def Scale(self, Scale: Scale):
        Scale.Apply(self)
        self.Scaled = Scale

        return self

    def Update(self):
        if self.Scaled:
            self.Scale(self.Scaled)
        if self.Docked:
            self.Dock(self.Docked)

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
            
        
        

        ## Update Children
        for Child in self.Children:
            Child: Widget

            Child.Update()

        ## Update Self
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)

        Position = self.Position + pygame.Vector2(self.Padding.left / 2, self.Padding.top / 2)
        Size = pygame.Rect(pygame.Vector2(0, 0), self.Size - pygame.Vector2(self.Padding.right / 2, self.Padding.bottom / 2))
        
        self.Surface.set_colorkey(pygame.Color(255, 0, 255))
        self.Parent.Surface.blit(self.Surface.convert_alpha(), Position, Size)
        
        self.Surface = pygame.Surface(self.Size) # recreate surface to reflect size changes (for responsive layouts)
            