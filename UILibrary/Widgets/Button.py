import pygame
import math

from .. import Utils
from ..Widget import Widget as Widget
from ..Theme import Theme


class Button(Widget):
    def __init__(self, Parent, Callback = None, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme: Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)

        self.Callback = Callback

    def SetCallback(self, Callback):
        self.Callback = Callback

    def Evaluate(self):
        super().Evaluate()

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

        if self.Selected:
            self.Surface.fill(self.Theme.Selected)

    def Update(self):
        super().Update()

class TextButton(Button):
    def __init__(self, Parent, Text, FontScale, Callback = None, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Callback, Position, Size, Theme)

        self.FontScale = FontScale
        self.Font = pygame.font.Font(self.Theme.Font, math.floor(self.Size.y * self.FontScale))

        self.Text = Text

    def Update(self):
        super().Evaluate()

        self.Font = pygame.font.Font(self.Theme.Font, math.floor(self.Size.y * self.FontScale))  
        Utils.TextWrapped(self.Surface, self.Text, self.Font, self.Theme.Foreground, self.Rect)

        super().Update()

class ImageButton(Button):
    def __init__(self, Parent: Widget, File, Callback = None, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Callback, Position, Size, Theme)

        self.Callback = Callback
        self.File = File

    def SetFile(self, File):
        self.File = File

    def Update(self):
        super().Evaluate()

        Image = pygame.image.load(self.File)
        Image = pygame.transform.scale(Image, self.Size)

        self.Surface.blit(Image, pygame.Vector2(0, 0))
        
        super().Update()



