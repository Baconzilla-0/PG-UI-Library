import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget


class Widget(Widget):
    def __init__(self, Parent: Widget, File, Callback = None, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)

        self.Callback = Callback
        self.File = File

    def SetFile(self, File):
        self.File = File

    def Update(self):
        Image = pygame.image.load(self.File)
        Image = pygame.transform.scale(Image, self.Size)
        
        if self.Clicked:
            if self.Callback:
                self.Callback()

        self.Surface.blit(Image, pygame.Vector2(0, 0))
        super().Update()
