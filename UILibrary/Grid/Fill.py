import pygame

class Fill:
    def __init__(self, Directions: pygame.Vector2):
        self.Directions = Directions

    def Apply(self, Widget):
        Rect: pygame.Rect = Widget.Parent.PaddingRect

        X = Rect.width
        Y = Rect.height

        for Child in Widget.Parent.Children:
            if Child != Widget:
                X -= self.Directions.x * Child.Size.x
                Y -= self.Directions.y * Child.Size.y

        Size = pygame.Vector2(X, Y)
        Widget.SetSize(Size)

        #Widget.Update()