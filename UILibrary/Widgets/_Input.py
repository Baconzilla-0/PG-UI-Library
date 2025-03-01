import pygame

from .. import Helpers
from ..Components import Widget as Widget

class Input(Widget):
    def __init__(self, Parent: Widget, Placeholder: str, FontScale = 0, Position = pygame.Vector2(10, 10), Size = pygame.Vector2(100, 100)):
        super().__init__(Parent, Position, Size)
        self.FontScale = FontScale
        self.Placeholder = Placeholder
        self.Text = ""

    def Update(self, Event: pygame.event.Event = None):
        self.Font = pygame.font.Font(self.Theme.Font, int(self.Size.y * self.FontScale))

        if self.Focused:
            for Event in self.GetRoot().Inputs.Events:
                if Event != None:
                    if Event.type == pygame.KEYDOWN:
                        # Check for backspace
                        if Event.key == pygame.K_BACKSPACE:
                            self.Text = self.Text[:-1]
                        elif Event.key == pygame.K_RETURN:
                            self.Focused = False
                        else:
                            self.Text += Event.unicode

        Helpers.blit_text(self.Surface, self.Text, pygame.Vector2(0,0), self.Font, self.Theme.Foreground, self.PaddingRect)
        super().Update()


