import pygame

from ..Theme import Theme
from ..Widget import Widget as Widget
from .Button import Button as Button

class List(Widget):
    def __init__(self, Parent: Widget, Position: pygame.Vector2 = pygame.Vector2(10, 10), Size: pygame.Vector2 = pygame.Vector2(100, 100), Spacing = None, Theme = None):
        super().__init__(Parent, Theme or Parent.Theme, Position, Size)
        if Spacing != None:
            self.Spacing = Spacing 
        else:
            self.Spacing = self.Theme.Spacing

    def Update(self):
        self.Surface.fill(self.Theme.ButtonHovered)

        x_offset = 0
        y_offset = 0
        
        highest = 0

        previous = None
        for child in self.Children:
            child: Widget
            child.Docked = None
            child.Padding = pygame.Rect(self.Spacing, self.Spacing, self.Spacing, self.Spacing)

            if x_offset + child.Size.y > self.Size.x:
                x_offset = 0
                if previous != None:
                    y_offset += previous.Size.y
                #highest = 0
            #else:
                #if highest < child.Size.y:
                #    highest += child.Size.y

            child.Position = pygame.Vector2(x_offset, y_offset)

            x_offset += child.Size.x

            previous = child
            

        super().Update()


class Panel(List):
    def __init__(self, Parent: Widget, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100), Spacing: int = None, Theme: Theme = None,):
        super().__init__(Parent, Position, Size, Spacing, Theme)
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
