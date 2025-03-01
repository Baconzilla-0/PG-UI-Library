import pygame
from pygame import Vector2, Color

import math

from .. import Helpers
from ..Components import Widget
from ..Components import TextWidget
from ..Components import ImageWidget


class Button(Widget):
    def __init__(self, Parent: Widget, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Interactive = True

    def Evaluate(self):
        super().Evaluate()

        if self.Clicked:
            if self.Callback:
                self.Callback()
            
    def Update(self):
        super().Update()


class TextButton(TextWidget):
    def __init__(self, Parent, Text = "Text", Position = Vector2(10, 10), Size = Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Interactive = True

        self.SetText(Text)

    def Evaluate(self):
        super().Evaluate()

        if self.Clicked:
            if self.Callback:
                self.Callback()

    def Update(self):

        super().Update()


class ImageButton(ImageWidget):
    def __init__(self, Parent: Widget, File, Position = Vector2(10, 10), Size = Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Interactive = True

        self.SetFile(File)

    def Evaluate(self):
        super().Evaluate()

        if self.Clicked:
            if self.Callback:
                self.Callback()

    def Update(self):
        super().Update()



