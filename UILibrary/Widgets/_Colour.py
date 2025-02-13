import pygame
import math

from .. import Helpers
from ..Widget import Widget as Widget
from ..Grid import Compass, Constraints, Divisions
from ..Grid import Scale

from ._Slider import Slider
from ._List import List
from ._Frame import Frame

class RGBPicker(Widget):
    def __init__(self, Parent, Position=pygame.Vector2(10, 10), Size=pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Colour = pygame.Color(0, 0, 0)

        self.ColourDisplay = Frame(self).Scale(Divisions.TW).Dock(Compass.E).Absolute()
        self.Container = List(self).Scale(Scale(pygame.Vector2(1.5, 1))).Dock(Compass.W).Absolute()
        self.RSlider = Slider(self.Container, 1, 255, Handle = pygame.Color(255, 0, 0)).Scale(Divisions.WT).Dock(Compass.N)
        self.GSlider = Slider(self.Container, 1, 255, Handle = pygame.Color(0, 255, 0)).Scale(Divisions.WT).Dock(Compass.C)
        self.BSlider = Slider(self.Container, 1, 255, Handle = pygame.Color(0, 0, 255)).Scale(Divisions.WT).Dock(Compass.S)
        #self.Slider.Ignore = True


    def Update(self):
        #Utils.Text(self.Surface, f"{self.Label} {self.Slider.Value.x}", self.Theme.Font, self.Theme.Foreground, (self.Size.y / 2) * 0.6, self.PaddingRect.topleft)
        
        self.Colour = pygame.Color(int(self.RSlider.Value.x), int(self.GSlider.Value.x), int(self.BSlider.Value.x))
        self.ColourDisplay.Theme.Background = self.Colour

        super().Update()