import pygame

from ..Style import Sheet
from ..Widget import Widget as Widget
#from ..Window import Widget as Window

class Screen(Widget):
    def __init__(self, Style: Sheet, Update = None):
        self.OnUpdate = Update
        super().__init__(None, Style, pygame.Vector2(0, 0), pygame.Vector2(0, 0))

    def SetParent(self, Parent):
        self.Parent = Parent
        self.Style = Parent.Style
        self.Surface = Parent.Surface

    def Update(self):
        if self.OnUpdate != None:
            self.OnUpdate()

        self.Size = self.Parent.Surface.get_size()
        pygame.draw.rect(self.Surface, self.Theme.Background, self.Rect)
        
        super().Update()
