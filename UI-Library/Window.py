import pygame

from .Theme import Theme
from .Widgets.Screen import Widget as Screen

class Widget:
    def __init__(self, Theme: Theme, Title: str, Position: pygame.Vector2, Size: pygame.Vector2, Resize = True, Icon = None):
        self.Theme = Theme
        self.Position = Position
        self.Resize = (lambda: pygame.RESIZABLE if Resize else 0)()
        self.Title = Title
        self.Icon = Icon
        self.Size = Size

        self.Load()
        

        self.Children = []
        self.Active = False
        self.ZIndex = 1

        self.Screen = None

    def Load(self):
        self.Surface = pygame.display.set_mode(self.Size, self.Resize) 
        pygame.display.set_caption(self.Title) 
        
        if self.Icon != None:
            Surface = pygame.image.load(self.Icon) 
            pygame.display.set_icon(Surface)

    def SetScreen(self, Screen: Screen):
        self.Screen = Screen
        Screen.SetParent(self)


    def Loop(self):
        self.Active = True
        
        if self.Screen != None:
            while self.Active: 
                self.Surface.fill(self.Theme.Background) 
                self.Screen.Update()

                pygame.display.update()

                for event in pygame.event.get():
    
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        self.Active = False
            
                
