import pygame

from ..Widget import Widget as Widget
from .. import Utils

class Frame(Widget):
    def __init__(self, Parent: Widget, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)

    def Update(self):
        #Shift = self.ZIndex * self.Theme.ZIndexShift
        #Colour = self.Theme.Background
        #Utils.Box(self, self.Theme.BackgroundInset)
        #pygame.draw.rect(self.Surface, pygame.Color(Colour.r + Shift, Colour.g + Shift, Colour.b + Shift), self.MarginRect)

        super().Update()
