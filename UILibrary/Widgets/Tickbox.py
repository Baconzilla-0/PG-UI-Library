import pygame
import math

from .. import Utils
from ..Widget import Widget as Widget
from .Image import Image
from ..Grid import Divisions, Compass, Constraints

class Tickbox(Image):
    def __init__(self, Parent: Widget, State = False, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Utils.GetFile(__file__, "../Assets/Tick.png"), Position, Size)
        self.Constrain(Constraints.SH)
        self.Value = State

    def Evaluate(self):
        
        super().Evaluate()

        if self.Clicked:

            if self.Value == False:
                self.Value = True
                self.SetFile(Utils.GetFile(__file__, "../Assets/Tick.png"))
            else:
                self.Value = False
                self.SetFile(Utils.GetFile(__file__, "../Assets/Cross.png"))

            
    def Update(self):
        super().Update()

class LabeledTickbox(Widget):
    def __init__(self, Parent, Label, State = False, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Parent.Style, Position, Size)

        self.Tickbox = Tickbox(self, State).Scale(Divisions.WY).Dock(Compass.E)
        self.Label = Label

    def Update(self):
        Utils.Text(self.Surface, f"{self.Label}", self.Theme.Font, self.Theme.Foreground, (self.Size.y) * 0.6, self.PaddingRect.topleft)
        self.Tickbox.Update()
        super().Update()
