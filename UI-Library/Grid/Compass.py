import pygame

from .Alignment import Alignment


C = Alignment(pygame.Vector2(0.5, 0.5), pygame.Vector2(0.5, 0.5)) # Centered

## Cardinal Directions
N = Alignment(pygame.Vector2(0.5, 0), pygame.Vector2(0.5, 0)) # North | Top
E = Alignment(pygame.Vector2(1, 0.5), pygame.Vector2(1, 0.5)) # East  | Right
S = Alignment(pygame.Vector2(0.5, 1), pygame.Vector2(0.5, 1)) # South | Bottom
W = Alignment(pygame.Vector2(0, 0.5), pygame.Vector2(0, 0.5)) # West  | Left

## Ordinal Directions
NE = Alignment(pygame.Vector2(1, 0), pygame.Vector2(1, 0)) # North East | Top Right
SE = Alignment(pygame.Vector2(1, 1), pygame.Vector2(1, 1)) # South East | Bottom Right
NW = Alignment(pygame.Vector2(0, 0), pygame.Vector2(0, 0)) # North West | Top Left
SW = Alignment(pygame.Vector2(0, 1), pygame.Vector2(0, 1)) # South West | Bottom Left