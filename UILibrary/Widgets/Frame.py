import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget


class Frame(Widget):
    def __init__(self, Parent: Widget, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)

    def Update(self):
        Shift = self.ZIndex * self.Theme.ZIndexShift
        Colour = self.Theme.Background

        pygame.draw.rect(self.Surface, pygame.Color(Colour.r + Shift, Colour.g + Shift, Colour.b + Shift), self.Rect)

        super().Update()
