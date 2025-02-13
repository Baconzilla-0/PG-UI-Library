import pygame
import math

from .. import Utils
from ..Widget import Widget as Widget


class Button(Widget):
    def __init__(self, Parent: Widget, Callback = None, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)

        self.Callback = Callback

    def SetCallback(self, Callback):
        self.Callback = Callback

    def Evaluate(self):
        super().Evaluate()

        if self.Clicked:
            if self.Callback:
                self.Callback()

        '''
        if self.Holding:
            
            Utils.Box(self, self.Theme.ButtonPressed)

        

        elif self.Hovered:
            Utils.Box(self, self.Theme.ButtonHovered)

        else:
            Utils.Box(self, self.Theme.ButtonIdle)

        if self.Selected:
            Utils.Box(self, self.Theme.Selected)
        '''
            
    def Update(self):
        super().Update()


class TextButton(Button):
    def __init__(self, Parent: Widget, Text, FontScale, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, None, Position, Size)

        self.FontScale = FontScale
        self.Font = pygame.font.Font(self.Theme.Font, math.floor(self.Size.y * self.FontScale))

        self.Text = Text

    def SetText(self, Text: str):
        self.Text = Text

    def Update(self):
        super().Evaluate()

        self.Font = pygame.font.Font(self.Theme.Font, math.floor(self.Size.y * self.FontScale))
        Utils.blit_text(self.Surface, self.Text, pygame.Vector2(0,0), self.Font, self.Theme.Foreground, self.PaddingRect)
        super().Update()


class ImageButton(Button):
    def __init__(self, Parent: Widget, File, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, None, Position, Size)
        self.File = File

    def SetFile(self, File):
        self.File = File

    def Update(self):
        super().Evaluate()

        Image = pygame.image.load(self.File)
        Image = pygame.transform.scale(Image, (abs(self.Size.x), abs(self.Size.y)))

        self.Surface.blit(Image, pygame.Vector2(0, 0))
        
        super().Update()



