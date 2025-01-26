import pygame

class Theme:
    def __init__(self):
        self.Background = pygame.Color(160, 160, 160)
        self.BackgroundInset = pygame.Color(140, 140, 140)
        self.ZIndexShift = -10

        self.ButtonIdle = pygame.Color(180, 180, 180)
        self.ButtonHovered = pygame.Color(200, 200, 200)
        self.ButtonPressed = pygame.Color(120, 120, 120)

        self.InputIdle = pygame.Color(180, 180, 180)
        self.InputHovered = pygame.Color(200, 200, 200)
        self.InputFocused = pygame.Color(120, 120, 120)

        self.Selected = pygame.Color(180, 180, 255)

        self.List = pygame.Color(140, 140, 140)
        self.Scrollbar = pygame.Color(100, 100, 100)

        self.Foreground = pygame.Color(15, 15, 15)

        self.Spacing = 10

        self.Font = ""