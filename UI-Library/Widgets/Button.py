import pygame
import math

from .. import Utils
from ..Widget import Widget as Widget

class Widget(Widget):
    def __init__(self, Parent: Widget, Text: str, FontScale, Callback = None, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)

        self.FontScale = FontScale
        self.Font = pygame.font.SysFont(self.Theme.Font, math.floor(self.Size.y * self.FontScale))

        self.Text = Text
        self.Callback = Callback

    def SetCallback(self, Callback):
        self.Callback = Callback


    def Update(self):
        self.Font = pygame.font.SysFont(self.Theme.Font, math.floor(self.Size.y * self.FontScale))

        if self.Holding:
            self.Surface.fill(self.Theme.ButtonPressed)

        elif self.Clicked:
            self.Surface.fill(self.Theme.ButtonPressed)
            if self.Callback:
                self.Callback()

        elif self.Hovered:
            self.Surface.fill(self.Theme.ButtonHovered)

        else:
            self.Surface.fill(self.Theme.ButtonIdle)

        Utils.TextWrapped(self.Surface, self.Text, self.Font, self.Theme.Foreground, self.Rect)        

        super().Update()


