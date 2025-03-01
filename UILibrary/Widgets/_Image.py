import pygame
import os

from ..Components import Widget as Widget
from ..Components import ImageWidget
from .. import Helpers

class Image(ImageWidget):
    def __init__(self, Parent: Widget, File, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.SetFile(File)

    def Update(self):
        
        super().Update()


class Animation(Widget):
    
    def __init__(self, Parent: Widget, File, FrameHeight: int, FrameTime: int, Callback, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Frame = 0
        self.Time = 0
        self.Done = False
        self.Callback = Callback
        self.FrameHeight = FrameHeight
        self.FrameTime = FrameTime
        self.File = File
        self.Image = pygame.image.load(self.File).convert_alpha() #.set_colorkey(pygame.Color(0, 0, 0, 0))
        self.Frames = self.Image.get_height() // self.FrameHeight

    def SetFile(self, File):
        self.File = File
        self.Image = pygame.image.load(self.File)
        self.Frames = self.Image.get_height() // self.FrameHeight

    def Update(self):
        self.Time += 1
        if self.Frame >= self.Frames:
            if not self.Done:
                self.Done = True
                self.Callback()
            return None
        
        
        Image = self.Image.subsurface(pygame.Rect(0, self.Frame * self.FrameHeight, self.Image.get_width(), self.FrameHeight))
        if self.Time >= self.FrameTime:
            self.Frame += 1
            self.Time = 0
        #try:
        Image = pygame.transform.scale(Image, self.Size)
        #except:
        #    pass
        #Image.set_colorkey(pygame.Color(0, 0, 0, 255))
        #self.Surface.fill(pygame.Color(255, 0, 0, 0))
        self.Surface.blit(Image, pygame.Vector2(0, 0), special_flags=pygame.BLEND_ALPHA_SDL2)
        super().Update()
    

