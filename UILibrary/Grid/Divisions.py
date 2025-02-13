import pygame

from .Scale import Scale

## Whole Variants
WW = Scale(pygame.Vector2(1, 1)) # Whole x Whole
WX = Scale(pygame.Vector2(1, 0)) # Whole x Whole
WY = Scale(pygame.Vector2(0, 1)) # Whole x Whole

## Half Variants
WH = Scale(pygame.Vector2(1, 2)) # Whole x Half
HW = Scale(pygame.Vector2(2, 1)) # Half x Whole
HH = Scale(pygame.Vector2(2, 2)) # Half x Half

HX = Scale(pygame.Vector2(2, 0)) # Half Horizontal
HY = Scale(pygame.Vector2(0, 2)) # Half Vertical

## Third Variants
TW = Scale(pygame.Vector2(3, 1)) # Third x Whole
WT = Scale(pygame.Vector2(1, 3)) # Whole x Third

TH = Scale(pygame.Vector2(3, 2)) # Third x Half
HT = Scale(pygame.Vector2(2, 3)) # Half x Third

TT = Scale(pygame.Vector2(3, 3)) # Third x Third


## Quarter Variants
QW = Scale(pygame.Vector2(4, 1)) # Quarter x Whole
WQ = Scale(pygame.Vector2(1, 4)) # Whole x Quarter

QH = Scale(pygame.Vector2(4, 2)) # Quarter x Half
HQ = Scale(pygame.Vector2(2, 4)) # Half x Quarter

QT = Scale(pygame.Vector2(4, 3)) # Quarter x Third
TQ = Scale(pygame.Vector2(4, 3)) # Third x Quarter

QQ = Scale(pygame.Vector2(4, 4)) # Quarter x Quarter


## Fifth Variants
WF = Scale(pygame.Vector2(1, 5)) # Whole x Fifth
FW = Scale(pygame.Vector2(5, 1)) # Fifth x Whole

HF = Scale(pygame.Vector2(2, 5)) # Half x Fifth
FH = Scale(pygame.Vector2(5, 2)) # Fifth x Half

TF = Scale(pygame.Vector2(3, 5)) # Third x Fifth
FT = Scale(pygame.Vector2(5, 3)) # Fifth x Third

QF = Scale(pygame.Vector2(4, 5)) # Quarter x Fifth
FQ = Scale(pygame.Vector2(5, 4)) # Fifth x Quarter

FF = Scale(pygame.Vector2(5, 5)) # Fifth x Fifth

## Sixth Variants
WS = Scale(pygame.Vector2(1, 6)) # Whole x Sixth
SW = Scale(pygame.Vector2(6, 1)) # Sixth x Whole

HS = Scale(pygame.Vector2(2, 6)) # Half x Sixth
SH = Scale(pygame.Vector2(6, 2)) # Sixth x Half

TS = Scale(pygame.Vector2(3, 6)) # Third x Sixth
ST = Scale(pygame.Vector2(6, 3)) # Sixth x Third

QS = Scale(pygame.Vector2(4, 6)) # Quarter x Sixth
SQ = Scale(pygame.Vector2(6, 4)) # Sixth x Quarter

FS = Scale(pygame.Vector2(5, 6)) # Fifth x Sixth
SF = Scale(pygame.Vector2(6, 5)) # Sixth x Fifth

SS = Scale(pygame.Vector2(6, 6)) # Sixth x Sixth


## Seventh Variants
WSe = Scale(pygame.Vector2(1, 7)) # Whole x Seventh
SeW = Scale(pygame.Vector2(7, 1)) # Seventh x Whole

HSe = Scale(pygame.Vector2(2, 7)) # Half x Seventh
SeH = Scale(pygame.Vector2(7, 2)) # Seventh x Half

TSe = Scale(pygame.Vector2(3, 7)) # Third x Seventh
SeT = Scale(pygame.Vector2(7, 3)) # Seventh x Third

QSe = Scale(pygame.Vector2(4, 7)) # Quarter x Seventh
SeQ = Scale(pygame.Vector2(7, 4)) # Seventh x Quarter

FSe = Scale(pygame.Vector2(5, 7)) # Fifth x Seventh
SeF = Scale(pygame.Vector2(7, 5)) # Seventh x Fifth

SSe = Scale(pygame.Vector2(6, 7)) # Sixth x Seventh
SeS = Scale(pygame.Vector2(7, 6)) # Seventh x Sixth

SeSe = Scale(pygame.Vector2(7, 7)) # Seventh x Seventh


## Eighth Variants
WE = Scale(pygame.Vector2(1, 8)) # Whole x Eighth
EW = Scale(pygame.Vector2(8, 1)) # Eighth x Whole

HE = Scale(pygame.Vector2(2, 8)) # Half x Eighth
EH = Scale(pygame.Vector2(8, 2)) # Eighth x Half

TE = Scale(pygame.Vector2(3, 8)) # Third x Eighth
ET = Scale(pygame.Vector2(8, 3)) # Eighth x Third

QE = Scale(pygame.Vector2(4, 8)) # Quarter x Eighth
EQ = Scale(pygame.Vector2(8, 4)) # Eighth x Quarter

FE = Scale(pygame.Vector2(5, 8)) # Fifth x Eighth
EF = Scale(pygame.Vector2(8, 5)) # Eighth x Fifth

SE = Scale(pygame.Vector2(6, 8)) # Sixth x Eighth
ES = Scale(pygame.Vector2(8, 6)) # Eighth x Sixth

SeE = Scale(pygame.Vector2(7, 8)) # Seventh x Eighth
ESe = Scale(pygame.Vector2(8, 7)) # Eighth x Seventh

EE = Scale(pygame.Vector2(8, 8)) # Eighth x Eighth


## Ninth Variants
WN = Scale(pygame.Vector2(1, 9)) # Whole x Ninth
NW = Scale(pygame.Vector2(9, 1)) # Ninth x Whole

HN = Scale(pygame.Vector2(2, 9)) # Half x Ninth
NH = Scale(pygame.Vector2(9, 2)) # Ninth x Half

TN = Scale(pygame.Vector2(3, 9)) # Third x Ninth
NT = Scale(pygame.Vector2(9, 3)) # Ninth x Third

QN = Scale(pygame.Vector2(4, 9)) # Quarter x Ninth
NQ = Scale(pygame.Vector2(9, 4)) # Ninth x Quarter

FN = Scale(pygame.Vector2(5, 9)) # Fifth x Ninth
NF = Scale(pygame.Vector2(9, 5)) # Ninth x Fifth

SN = Scale(pygame.Vector2(6, 9)) # Sixth x Ninth
NS = Scale(pygame.Vector2(9, 6)) # Ninth x Sixth

SeN = Scale(pygame.Vector2(7, 9)) # Seventh x Ninth
NSe = Scale(pygame.Vector2(9, 7)) # Ninth x Seventh

EN = Scale(pygame.Vector2(8, 9)) # Eighth x Ninth
NE = Scale(pygame.Vector2(9, 8)) # Ninth x Eighth

NN = Scale(pygame.Vector2(9, 9)) # Ninth x Ninth


## Tenth Variants
WTe = Scale(pygame.Vector2(1, 10)) # Whole x Tenth
TeW = Scale(pygame.Vector2(10, 1)) # Tenth x Whole

HTe = Scale(pygame.Vector2(2, 10)) # Half x Tenth
TeH = Scale(pygame.Vector2(10, 2)) # Tenth x Half

TTe = Scale(pygame.Vector2(3, 10)) # Third x Tenth
TeT = Scale(pygame.Vector2(10, 3)) # Tenth x Third

QTe = Scale(pygame.Vector2(4, 10)) # Quarter x Tenth
TeQ = Scale(pygame.Vector2(10, 4)) # Tenth x Quarter

FTe = Scale(pygame.Vector2(5, 10)) # Fifth x Tenth
TeF = Scale(pygame.Vector2(10, 5)) # Tenth x Fifth

STe = Scale(pygame.Vector2(6, 10)) # Sixth x Tenth
TeS = Scale(pygame.Vector2(10, 6)) # Tenth x Sixth

SeTe = Scale(pygame.Vector2(7, 10)) # Seventh x Tenth
TeSe = Scale(pygame.Vector2(10, 7)) # Tenth x Seventh

ETe = Scale(pygame.Vector2(8, 10)) # Eighth x Tenth
TeE = Scale(pygame.Vector2(10, 8)) # Tenth x Eighth

NTe = Scale(pygame.Vector2(9, 10)) # Ninth x Tenth
TeN = Scale(pygame.Vector2(10, 9)) # Tenth x Ninth

TeTe = Scale(pygame.Vector2(10, 10)) # Tenth x Tenth