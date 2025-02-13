import pygame

from .. import Utils
from ..Widget import Widget as Widget

class Input(Widget):
    def __init__(self, Parent: Widget, Placeholder: str, FontScale, Callback = None, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.FontScale = FontScale
        self.Placeholder = Placeholder
        self.Text = ""

        self.Callback = Callback

    def SetCallback(self, Callback):
        self.Callback = Callback

    def Update(self, Event: pygame.event.Event = None):
        self.Font = pygame.font.Font(self.Theme.Font, self.Size.y * self.FontScale)

        #if self.Hovered == False:
            #self.Surface.fill(self.Theme.InputIdle)
        #elif self.Hovered:
            #self.Surface.fill(self.Theme.InputHovered)
        if self.Focused:
            #self.Surface.fill(self.Theme.InputFocused)

            for Event in pygame.event.get():
                if Event != None:
                    if Event.type == pygame.KEYDOWN:
                        # Check for backspace
                        if Event.key == pygame.K_BACKSPACE:
                            self.Text = self.Text[:-1]
                        elif Event.key == pygame.K_RETURN:
                            self.Focused = False
                        else:
                            self.Text += Event.unicode

        Utils.blit_text(self.Surface, self.Text, pygame.Vector2(0,0), self.Font, self.Theme.Foreground, self.PaddingRect)
        super().Update()


