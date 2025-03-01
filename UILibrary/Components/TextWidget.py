from pygame import Vector2, Color, Rect
import pygame

from .Widget import Widget

class TextWidget(Widget):
    def __init__(self, Parent, Position=..., Size=..., Name="Widget"):
        self.Text = "Text"
        super().__init__(Parent, Position, Size, Name)
        
        self.SetText("Shart")

    def SetText(self, Text):
        self.Text = Text

        self.Changed()

    def Changed(self):
        super().Changed()

        print("Text area changed")
        self.TextArea = Rect(Vector2(0, 0), self.PaddingRect.size)
        self.TextHeight = (self.TextArea.height) * ( 72 / 96 ) 
        self.FontFile = pygame.font.Font(self.Theme.Font, int(self.TextHeight))
           
        Width = 0
        for Char in self.Text:
            Individual = self.FontFile.size(Char)[0]
            Width += Individual

        Scale = self.TextHeight / Width
        
        Goal = self.TextArea.width
        if Width > Goal:
            self.FontFile = pygame.font.Font(self.Theme.Font, int(Scale * Goal))

        self.TextSurface = self.FontFile.render(self.Text, True, self.Theme.Foreground)

    def Evaluate(self):
        super().Evaluate()

    def Update(self):
        self.Surface.blit(self.TextSurface, (self.PaddingRect.left, 0))

        super().Update()