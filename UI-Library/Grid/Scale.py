import pygame

class Scale:
    def __init__(self, Size: pygame.Vector2):
        self.Size = Size

    def Apply(self, Widget):
        Rect = Widget.Parent.Surface.get_rect()

        X = Rect.width * self.Size.x
        Y = Rect.height * self.Size.y

        Size = pygame.Vector2(X, Y)
        Widget.Size = Size

        #Widget.Update()