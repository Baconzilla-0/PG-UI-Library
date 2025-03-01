import pygame
import math

from .. import Helpers
from ..Components import Widget
from ..Components import ImageWidget


from ..Grid import Compass, Constraints, Divisions

class Tickbox(ImageWidget):
    def __init__(self, Parent: Widget, State = False, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, None, Position, Size)
        self.Constrain(Constraints.SH)
        self.Interactive = True
        self.Value = State

        if self.Value == True:
            self.SetFile(Helpers.GetFile(__file__, "../Assets/Tick.png"))
        else:
            self.SetFile(Helpers.GetFile(__file__, "../Assets/Cross.png"))

    def Evaluate(self):
        
        super().Evaluate()

        if self.Clicked:
            
            if self.Value == False:
                self.Value = True
                self.SetFile(Helpers.GetFile(__file__, "../Assets/Tick.png"))
            else:
                self.Value = False
                self.SetFile(Helpers.GetFile(__file__, "../Assets/Cross.png"))
            
            print(self.Value)
            if self.Callback:
                self.Callback()

            
    def Update(self):
        if self.ImageSurface != None:
            pass
        else:
            if self.Value == True:
                Helpers.Box(self, Colour=pygame.Color(0, 200, 0))
            else:
                Helpers.Box(self, Colour=pygame.Color(200, 0, 0))

        super().Update()

class LabeledTickbox(Widget):
    def __init__(self, Parent, Label, State = False, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Parent.Style, Position, Size)

        self.Tickbox = Tickbox(self, State).Scale(Divisions.WY).Dock(Compass.E)
        self.Label = Label

    def Update(self):
        Helpers.Text(self.Surface, f"{self.Label}", self.Theme.Font, self.Theme.Foreground, self.PaddingRect.topleft, (self.Size.x - self.Tickbox.Size.x, self.PaddingRect.height))
        self.Tickbox.Update()
        super().Update()
