import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget


class Widget(Widget):
    def __init__(self, Parent: Widget, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)

    def Update(self):
        self.Surface.fill(self.Theme.ButtonHovered)

        x_offset = 0
        y_offset = 0
        for child in self.Children:
            child: Widget
            child.Docked = None
            child.Padding = pygame.Rect(self.Theme.Spacing, self.Theme.Spacing, self.Theme.Spacing, self.Theme.Spacing)

            if x_offset + child.Size.y > self.Size.x:
                x_offset = 0
                y_offset += child.Size.y

            child.Position = pygame.Vector2(x_offset, y_offset)

            x_offset += child.Size.x
            

        super().Update()
