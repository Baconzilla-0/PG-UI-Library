import pygame
import math

from .. import Utils
from ..Widget import Widget as Widget

class Widget(Widget):
    def __init__(self, Parent: Widget, Text: str, FontScale, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)
        self.Text = Text

        self.FontScale = FontScale
        self.Font = pygame.font.SysFont(self.Theme.Font, math.floor(self.Size.y * self.FontScale))

    def SetText(self, Text):
        self.Text = Text

    def Update(self):
        self.Surface.fill(self.Theme.Background)
        self.Font = pygame.font.SysFont(self.Theme.Font, math.floor(self.Size.y * self.FontScale))

        Utils.TextWrapped(self.Surface, self.Text, self.Font, self.Theme.Foreground, self.Rect)
        

        super().Update()


