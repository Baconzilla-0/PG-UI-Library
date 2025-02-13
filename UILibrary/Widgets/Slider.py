import pygame
import math

from .. import Utils
from ..Widget import Widget as Widget
from ..Grid import Divisions, Compass, Constraints


class Slider(Widget):
    def __init__(self, Parent: Widget, Minimum = 0, Maximum = 100, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100), Handle = pygame.Color(255, 0, 0)):
        super().__init__(Parent, Position, Size)

        self.Handle = Handle
        self.Maximum = Maximum
        self.Minimum = Minimum
        self.HandleSize = pygame.Vector2(20, 20)
        self.InternalValue = pygame.Vector2(0, 0)
        self.Value = pygame.Vector2(Minimum, Minimum)

        self.Started = False
        self.Offset = (self.MouseStart - self.InternalValue)
        self.Interactive = True

    def MoveHandle(self, Position: pygame.Vector2):
        XPos = max(0, min(self.MarginRect.width - self.HandleSize.x, Position.x))
        YPos = max(0, min(self.MarginRect.height - self.HandleSize.y, Position.y))

        #AbsMouse = pygame.mouse.get_pos()
        #pygame.event.clear()
        #pygame.mouse.set_pos((AbsMouse[0], self.AbsolutePosition.y))

        self.InternalValue = pygame.Vector2(XPos, YPos)

    def Evaluate(self):
        
        super().Evaluate()

        
        if self.Holding:
            if not self.Started:
                self.Offset = (self.MouseStart - self.InternalValue)

            self.Started = True
            self.MoveHandle(self.RelativeMouse )
        else:
            self.Started = False

            
    def Update(self):
        self.HandleSize = pygame.Vector2(self.PaddingRect.height + 5, self.PaddingRect.height + 5)
        Utils.Box(self, self.Handle, Rect=pygame.Rect(self.InternalValue, self.HandleSize))
        
        HalfHandleX = self.HandleSize.x / 2
        XConstriant = (HalfHandleX, self.MarginRect.width - self.HandleSize.x)
        XValue = self.InternalValue.x / XConstriant[1]
        ScaledX = XValue * self.Maximum

        HalfHandleY = self.HandleSize.y / 2
        YConstriant = (HalfHandleY, self.MarginRect.width - self.HandleSize.y)
        YValue = self.InternalValue.y / YConstriant[1]
        ScaledY = YValue * self.Maximum

        self.Value = pygame.Vector2(ScaledX, ScaledY)

        super().Update()

class LabeledSlider(Widget):
    def __init__(self, Parent, Label, Minimum=0, Maximum=100, Position=pygame.Vector2(10, 10), Size=pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)

        self.Slider = Slider(self, Minimum, Maximum).Scale(Divisions.WH).Dock(Compass.S)
        #self.Slider.Ignore = True

        self.Label = Label

    def Update(self):
        Utils.Text(self.Surface, f"{self.Label} {self.Slider.Value.x}", self.Theme.Font, self.Theme.Foreground, (self.Size.y / 2) * 0.6, self.PaddingRect.topleft)
        self.Slider.Update()
        super().Update()