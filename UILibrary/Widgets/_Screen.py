import pygame

from ..Style import Sheet
from ..Widget import Widget as Widget
#from ..Window import Widget as Window

class Screen(Widget):
    def __init__(self, Style: Sheet, Update = None):
        self.OnUpdate = Update
        super().__init__(None, pygame.Vector2(0, 0), pygame.Vector2(0, 0), Style=Style)

        #self.Root = True
        self.FocusedWidget = None

    def SetFocusedWidget(self, Widget: Widget):
        #Widget.Focused = False
        self.FocusedWidget = Widget

    def GetFocusedWidget(self):
        return self.FocusedWidget

    def Update(self):
        if self.OnUpdate != None:
            self.OnUpdate()

        self.Size = self.Parent.Surface.get_size()
        pygame.draw.rect(self.Surface, self.Theme.Background, self.Rect)
        
        super().Update()
