import pygame
import math

from .. import Helpers
from ..Widget import Widget as Widget
from ..Grid import Compass, Constraints, Divisions


class Slider(Widget):
    def __init__(self, Parent: Widget, Minimum = 0, Maximum = 100, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100), Handle = pygame.Color(255, 0, 0)):
        super().__init__(Parent, Position, Size)

        self.Handle = Handle
        self.Maximum = Maximum
        self.Minimum = Minimum
        self.HandleSize = pygame.Vector2(20, 20)
        self.AutoHandle = True
        self.InternalValue = pygame.Vector2(0, 0)
        self.Value = pygame.Vector2(Minimum, Minimum)

        self.Started = False
        self.Offset = (self.MouseStart - self.InternalValue)
        self.Interactive = True
    
    def SetValue(self, Value: pygame.Vector2):
        XConstriant = self.Size.x - self.HandleSize.x
        YConstriant = self.Size.y - self.HandleSize.y

        XValue = abs((Value.x + self.Minimum) / (self.Maximum - self.Minimum))
        YValue = abs((Value.y + self.Minimum) / (self.Maximum - self.Minimum))

        #print(XValue, XConstriant, YValue, YConstriant)

        self.InternalValue.x = XValue * XConstriant
        self.InternalValue.y = YValue * YConstriant

    def MoveHandle(self, Position: pygame.Vector2):
        XPos = max(0, min(self.MarginRect.width - self.HandleSize.x, Position.x))
        YPos = max(0, min(self.MarginRect.height - self.HandleSize.y, Position.y))

        self.InternalValue = pygame.Vector2(XPos, YPos)

    def Evaluate(self):
        
        super().Evaluate()

        
        if self.Holding:
            if not self.Started:
                self.Offset = (self.MouseStart - self.InternalValue)

            self.Started = True
            self.MoveHandle(self.RelativeMouse)
        else:
            self.Started = False

            
    def Update(self):
        if self.AutoHandle:
            self.HandleSize = pygame.Vector2(self.PaddingRect.height + 5, self.PaddingRect.height + 5)

        Helpers.Box(self, self.Handle, Rect=pygame.Rect(self.InternalValue, self.HandleSize))
        
        
        XConstriant = self.Size.x - self.HandleSize.x
        YConstriant = self.Size.y - self.HandleSize.y

        if YConstriant != 0 and XConstriant != 0:
            XValue = (self.InternalValue.x / XConstriant) * (self.Maximum - self.Minimum) + self.Minimum
            YValue = (self.InternalValue.y / YConstriant) * (self.Maximum - self.Minimum) + self.Minimum

            self.Value = pygame.Vector2(XValue, YValue)

        super().Update()



class LabeledSlider(Widget):
    def __init__(self, Parent, Label, Minimum=0, Maximum=100, Position=pygame.Vector2(10, 10), Size=pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)

        self.Slider = Slider(self, Minimum, Maximum).Scale(Divisions.WH).Dock(Compass.S)
        #self.Slider.Ignore = True

        self.Label = Label

    def Update(self):
        Helpers.Text(self.Surface, f"{self.Label} {self.Slider.Value.x}", self.Theme.Font, self.Theme.Foreground, (self.Size.y / 2) * 0.6, self.PaddingRect.topleft)
        self.Slider.Update()
        super().Update()