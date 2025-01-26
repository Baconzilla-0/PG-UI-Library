import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget


class Image(Widget):
    def __init__(self, Parent: Widget, File, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme: Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)

        self.File = File
        self.Image = pygame.image.load(self.File).convert_alpha()

    def SetFile(self, File):
        self.File = File
        self.Image = pygame.image.load(self.File).convert_alpha()

    def SetSize(self, Size: pygame.Vector2):
        super().SetSize(Size)
        self.Image = pygame.image.load(self.File).convert_alpha()

    def Evaluate(self):
        self.Image = pygame.transform.scale(self.Image, self.Size)
        return super().Evaluate()

    def Update(self):
        self.Surface.blit(self.Image, pygame.Vector2(0, 0))
        super().Update()

class Animation(Image):
    def __init__(self, Parent: Widget, File, FrameHeight: int, FrameTime: int, Callback, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Theme = None):
        super().__init__(Parent, File, Position, Size, Theme or Parent.Theme)

        self.Frame = 0
        self.Time = 0
        self.Done = False
        self.Callback = Callback

        self.FrameHeight = FrameHeight
        self.FrameTime = FrameTime
        self.FrameImage = None

        self.Frames = self.Image.get_height() // self.FrameHeight

    def SetFile(self, File):
        super().SetFile(File)
        self.Frames = self.Image.get_height() // self.FrameHeight

    def Evaluate(self):
        self.Time += 1
        if self.Frame >= self.Frames:
            if not self.Done:
                self.Done = True
                self.Callback()
            return None
        
        
        self.FrameImage = self.Image.subsurface(pygame.Rect(0, self.Frame * self.FrameHeight, self.Image.get_width(), self.FrameHeight))

        if self.Time >= self.FrameTime:
            self.Frame += 1
            self.Time = 0

        self.FrameImage = pygame.transform.scale(self.FrameImage, self.Size)

    def Update(self):
        self.Surface.blit(self.FrameImage, pygame.Vector2(0, 0), special_flags=pygame.BLEND_ALPHA_SDL2)
        
        super().Update()

