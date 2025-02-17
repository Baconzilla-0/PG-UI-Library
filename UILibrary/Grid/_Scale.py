import pygame

class Scale:
    def __init__(self, Size: pygame.Vector2):
        self.Size = Size

    def Apply(self, Widget):
        try:
            try:
                Rect = Widget.Parent.PaddingRect
            except Exception:
                Rect = Widget.Parent.Surface.get_rect()

            if self.Size.y != 0:
                Y = Rect.height / self.Size.y
            else:
                Y = Widget.Size.y
            if self.Size.x != 0:
                X = Rect.width / self.Size.x
            else:
                X = Widget.Size.x

            
            

            Size = pygame.Vector2(X, Y)
            Widget.SetSize(Size)
        except:
            pass
        #Widget.Update()