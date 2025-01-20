import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget


class Widget(Widget):
    def __init__(self, Parent: Widget, File, FrameHeight: int, FrameTime: int, Callback, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)

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

        Image = pygame.transform.scale(Image, self.Size)
        #Image.set_colorkey(pygame.Color(0, 0, 0, 255))
        #self.Surface.fill(pygame.Color(255, 0, 0, 0))
        self.Surface.blit(Image, pygame.Vector2(0, 0), special_flags=pygame.BLEND_ALPHA_SDL2)
        super().Update()
