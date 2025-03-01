import pygame

from ..Style import Sheet
from ..Components import Widget as Widget
#from ..Window import Widget as Window

class Screen(Widget):
    def __init__(self, Style: Sheet, Update = None):
        self.OnUpdate = Update
        super().__init__(None, pygame.Vector2(0, 0), pygame.Vector2(0, 0))
        self.Style = Style

        self.Interactive = False
        self.FocusedWidget = None

    

    def Update(self):
        if self.OnUpdate != None:
            self.OnUpdate()

        self.Generate()
        self.SetSize(self.Parent.Surface.get_size())
        pygame.draw.rect(self.Surface, self.Theme.Background, self.Rect)
        
        super().Update()
