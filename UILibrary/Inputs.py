import pygame

class Inputs:
    def __init__(self, Window):
        self.Mouse1 = False
        self.Mouse2 = False
        self.Mouse3 = False

        self.MousePosition = pygame.mouse.get_pos()

        self.Events = []

    def Update(self):
        self.Mouse = pygame.mouse.get_pressed()
        self.Mouse1 = self.Mouse[0]
        self.Mouse2 = self.Mouse[1]
        self.Mouse3 = self.Mouse[2]

        self.MousePosition = pygame.mouse.get_pos()

        self.Events = pygame.event.get()