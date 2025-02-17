import pygame

from ..Style import Sheet
from ..Widgets._Screen import Screen

from ..Inputs import Inputs

class Widget:
    def __init__(self, Style: Sheet, Title: str, Size: pygame.Vector2, Position: pygame.Vector2 = pygame.Vector2(0, 0), Resize = True, Icon = None):
        self.Style = Style
        self.Position = Position
        self.AbsolutePosition = pygame.Vector2(0, 0)
        self.Resize = (lambda: pygame.RESIZABLE if Resize else 0)()
        self.Title = Title
        self.Icon = Icon
        self.Size = Size

        self.Load()
        self.Inputs = Inputs(self)

        self.Root = True

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

    def GetRoot(self):
        if self.Root:
            return self
        else:
            print("something is very wrong.")

    def SetScreen(self, Screen: Screen):
        self.Screen = Screen
        Screen.SetParent(self)

    def Loop(self):
        self.Active = True

        if self.Screen != None:
            while self.Active: 
                #self.Surface.fill(self.Theme.Background) 
                self.Inputs.Update()
                self.Screen.Update()

                pygame.display.update()

                for Event in self.Inputs.Events:
                    Event: pygame.event.Event

                    if Event.type == pygame.QUIT:
                        pygame.quit()
                        self.Active = False
            
                
