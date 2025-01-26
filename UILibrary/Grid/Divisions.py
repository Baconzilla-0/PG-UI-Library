import pygame

from .Scale import Scale

## Whole Variants
WW = Scale(pygame.Vector2(1, 1)) # Whole x Whole
WX = Scale(pygame.Vector2(1, 0)) # Whole x Whole
WY = Scale(pygame.Vector2(0, 1)) # Whole x Whole

## Half Variants
WH = Scale(pygame.Vector2(1, 0.5)) # Whole x Half
HW = Scale(pygame.Vector2(0.5, 1)) # Half x Whole
HH = Scale(pygame.Vector2(0.5, 0.5)) # Half x Half

HX = Scale(pygame.Vector2(0.5, 0)) # Half Horizontal
HY = Scale(pygame.Vector2(0, 0.5)) # Half Vertical

## Third Variants
TW = Scale(pygame.Vector2(0.3, 1)) # Third x Whole
WT = Scale(pygame.Vector2(1, 0.3)) # Whole x Third

TH = Scale(pygame.Vector2(0.3, 0.5)) # Third x Half
HT = Scale(pygame.Vector2(0.5, 0.3)) # Half x Third

TT = Scale(pygame.Vector2(0.3, 0.3)) # Third x Third


## Quarter Variants
QW = Scale(pygame.Vector2(0.25, 1)) # Quarter x Whole
WQ = Scale(pygame.Vector2(1, 0.25)) # Whole x Quarter

QH = Scale(pygame.Vector2(0.25, 0.5)) # Quarter x Half
HQ = Scale(pygame.Vector2(0.5, 0.25)) # Half x Quarter

QT = Scale(pygame.Vector2(0.25, 0.3)) # Quarter x Third
TQ = Scale(pygame.Vector2(0.25, 0.3)) # Third x Quarter

QQ = Scale(pygame.Vector2(0.25, 0.25)) # Quarter x Quarter


## Fifth Variants
WF = Scale(pygame.Vector2(1, 0.2)) # Whole x Fifth
FW = Scale(pygame.Vector2(0.2, 1)) # Fifth x Whole

HF = Scale(pygame.Vector2(0.5, 0.2)) # Half x Fifth
FH = Scale(pygame.Vector2(0.2, 0.5)) # Fifth x Half

TF = Scale(pygame.Vector2(0.3, 0.2)) # Third x Fifth
FT = Scale(pygame.Vector2(0.2, 0.3)) # Fifth x Third

QF = Scale(pygame.Vector2(0.25, 0.2)) # Quarter x Fifth
FQ = Scale(pygame.Vector2(0.2, 0.25)) # Fifth x Quarter

FF = Scale(pygame.Vector2(0.2, 0.2)) # Fifth x Fifth