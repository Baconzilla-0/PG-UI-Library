import pygame
import math

from .. import Helpers
from ..Components import Widget as Widget

class Label(Widget):
    def __init__(self, Parent: Widget, Text: str, FontScale = 0, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Text = Text

        self.FontScale = FontScale
        self.Font = pygame.font.Font(self.Theme.Font, math.floor(self.Size.y * self.FontScale))

    def SetText(self, Text):
        self.Text = Text

    def Update(self):
        Helpers.Box(self, self.Theme.Background)

        self.Font = pygame.font.Font(self.Theme.Font, math.floor(self.Size.y * self.FontScale))
        #Utils.TextWrapped(self.Surface, self.Text, self.Font, self.Theme.Foreground, self.PaddingRect)
        Helpers.Text(self.Surface, self.Text, self.Theme.Font, self.Theme.Foreground, self.PaddingRect.topleft, self.PaddingRect.size)
        #Helpers.blit_text(self.Surface, self.Text, pygame.Vector2(0,0), self.Font, self.Theme.Foreground, self.PaddingRect)
        

        super().Update()


