import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget
#from ..Window import Widget as Window

class Screen(Widget):
    def __init__(self, Theme: Theme = None, Update = None):
        self.OnUpdate = Update
        super().__init__(None, Theme, pygame.Vector2(0, 0), pygame.Vector2(0, 0))

    def SetParent(self, Parent):
        self.Parent = Parent
        self.Theme = Parent.Theme
        self.Surface = Parent.Surface

    def Update(self):
        if self.OnUpdate != None:
            self.OnUpdate()

        self.Size = self.Parent.Surface.get_size()
        pygame.draw.rect(self.Surface, self.Theme.Background, self.Rect)
        
        super().Update()
