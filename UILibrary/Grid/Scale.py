import pygame

class Scale:
    def __init__(self, Size: pygame.Vector2):
        self.Size = Size

    def Apply(self, Widget):
        try:
            Rect = Widget.Parent.PaddingRect
        except Exception:
            Rect = Widget.Parent.Surface.get_rect()

        X = Rect.width * self.Size.x
        Y = Rect.height * self.Size.y

        X = X or Widget.Size.x
        Y = Y or Widget.Size.y

        Size = pygame.Vector2(X, Y)
        Widget.SetSize(Size)

        #Widget.Update()