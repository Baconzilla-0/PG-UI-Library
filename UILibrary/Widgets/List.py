import pygame
import math

from ..Widget import Widget as Widget
from .Button import Button as Button

class List(Widget):
    def __init__(self, Parent: Widget, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Parent.Style, Position, Size)

    def Evaluate(self):
        super().Evaluate()

        x_offset = 0
        y_offset = 0
        
        highest = 0

        previous = None
        for child in self.Children:
            child: Widget
            child.Docked = None

            if x_offset + child.Size.y > self.Size.x:
                x_offset = 0
                if previous != None:
                    y_offset += previous.Size.y

            child.Position = pygame.Vector2(x_offset, y_offset)

            x_offset += child.Size.x

            previous = child

    def Update(self):
        super().Update()

class Panel(List):
    def __init__(self, Parent: Widget, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.Selected: Button = None

    def Evaluate(self):
        for Index, Child in enumerate(self.Children):
            Child: Button
            if Child.Clicked:
                if self.Selected != None:
                    self.Selected.Selected = False

                if self.Selected != Child:
                    self.Selected = Child
                    self.Selected.Selected = True
                else:
                    self.Selected = None



    def Update(self):
        super().Update()

class ScrollList(List):
    def __init__(self, Parent: Widget, Position=pygame.Vector2(10, 10), Size=pygame.Vector2(100, 100), ScrollSpeed=20):
        super().__init__(Parent, Position, Size)
        self.ScrollSpeed = ScrollSpeed
        self.ScrollOffset = 0
        self.ScrollVelocity = 0

    def Scroll(self):
        if self.Hovered:
            for Event in pygame.event.get():
                if Event.type == pygame.MOUSEWHEEL:
                    self.ScrollVelocity += Event.y * self.ScrollSpeed
                    

    def Evaluate(self):
        super().Evaluate()

        total = 0
        for child in self.Children:
            child: Widget
            total += child.Size.y

        
        self.ScrollOffset += self.ScrollVelocity
        self.ScrollVelocity *= 0.8
        #self.ScrollVelocity -= 1 scrolling gravity

        ndifference = self.ScrollOffset - -(total/2)
        pdifference = self.ScrollOffset

        Friction = 70

        if self.ScrollOffset < -(total/2):
            #self.ScrollOffset = -(total/2)
            self.ScrollVelocity -= ndifference / Friction
        if self.ScrollOffset > 0:
            self.ScrollVelocity -= pdifference / Friction
            #self.ScrollOffset = 0

        y_offset = self.ScrollOffset + (self.PaddingRect.y / 2)
        for child in self.Children:
            child: Widget
            child.Position = pygame.Vector2(child.Position.x, y_offset)
            y_offset += child.Size.y

    def Update(self):
        self.Scroll()
        
        super().Update()

       
        