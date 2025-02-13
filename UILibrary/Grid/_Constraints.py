import pygame

from ._Fill import Fill
from ._Aspect import Aspect

A = Fill(pygame.Vector2(1, 1))
W = Fill(pygame.Vector2(1, 0))
H = Fill(pygame.Vector2(0, 1))

ASH = Aspect("Y", 1)
ASW = Aspect("X", 1)