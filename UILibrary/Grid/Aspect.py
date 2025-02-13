import pygame

class Aspect:
    def __init__(self, Axis: str, Scale: int):
        self.Scale = Scale
        self.Axis = Axis

    def Apply(self, Widget):
        try:
            Rect = Widget.Parent.PaddingRect
        except Exception:
            Rect = Widget.Parent.Surface.get_rect()

        if self.Axis == "X":
            Y = Rect.width * self.Scale
        else:
            Y = Rect.height
        if self.Axis == "Y":
            X = Rect.height * self.Scale
        else:
            X = Rect.width

        Size = pygame.Vector2(X, Y)
        Widget.SetSize(Size)

        #Widget.Update()