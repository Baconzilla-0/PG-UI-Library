import pygame

class Alignment:
    def __init__(self, Scale: pygame.Vector2, Anchor: pygame.Vector2):
        self.Scale = Scale
        self.Anchor = Anchor

    def Apply(self, Widget):
        Rect = Widget.Parent.Surface.get_rect()

        X = (Rect.width * self.Scale.x) - (Widget.Size.x * self.Anchor.x)
        Y = (Rect.height * self.Scale.y) - (Widget.Size.y * self.Anchor.y)

        Position = pygame.Vector2(X, Y)
        Widget.Position = Position
        #Widget.Update()