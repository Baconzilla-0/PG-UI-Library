from pygame import Vector2, Color, Rect
import pygame, os

from .Widget import Widget

class ImageWidget(Widget):
    def __init__(self, Parent, Position=..., Size=..., Name="Widget"):
        super().__init__(Parent, Position, Size, Name)
        self.RawSurface = pygame.Surface(self.Size)
        self.Changed()
        

    def SetFile(self, File: os.PathLike):
        self.ImageFile = File
        self.RawSurface = pygame.image.load(self.ImageFile)
        self.Changed()
    

    def Changed(self):
        super().Changed()
        print("Image display changed")

        try:
            self.ImageSurface = pygame.transform.scale(self.RawSurface, self.MarginRect.size)
        except:
            self.ImageSurface = self.RawSurface
        

    def Evaluate(self):
        super().Evaluate()

    def Update(self):
        self.Surface.blit(self.ImageSurface, (0,0))

        super().Update()