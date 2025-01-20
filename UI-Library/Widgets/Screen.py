import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget
#from ..Window import Widget as Window

class Widget(Widget):
    def __init__(self, Theme = None):
        super().__init__(None, Theme, pygame.Vector2(0, 0), pygame.Vector2(0, 0))

    def SetParent(self, Parent):
        self.Parent = Parent
        self.Theme = Parent.Theme
        self.Surface = Parent.Surface

    def Update(self):
        self.Size = self.Parent.Surface.get_size()
        pygame.draw.rect(self.Surface, self.Theme.Background, self.Rect)
        
        super().Update()
