import pygame

from ..Components import Widget as Widget
from .. import Helpers

class ProgressBar(Widget):
    def __init__(self, Parent: Widget, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Value = 50

    def SetValue(self, Value):
        self.Value = Value

    def Update(self):
        Rect = pygame.Rect(self.MarginRect.left, self.MarginRect.top, self.MarginRect.width * (self.Value / 100), self.MarginRect.height)
        Helpers.Box(self, self.Theme.Foreground, self.Theme.BorderColour, Rect)

        super().Update()

class Graph(Widget):
    def __init__(self, Parent: Widget, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Value = 50

    def SetValue(self, Value):
        self.Value = Value

    def Update(self):
        Rect = pygame.Rect(self.MarginRect.left, self.MarginRect.top, self.MarginRect.width * (self.Value / 100), self.MarginRect.height)
        Helpers.Box(self, self.Theme.Foreground, self.Theme.BorderColour, Rect)

        super().Update()
