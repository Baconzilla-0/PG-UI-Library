import pygame

import sys, os

def GetFile(Start, File: str):
    if getattr(sys, 'frozen', False):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(os.path.abspath(Start))
    return basedir + "/" + File

def Text(Surface: pygame.Surface, Text: str, Font: str, Colour: pygame.Color, Size: int, Position: pygame.Vector2): # A function to render text with a specified size, font, and position
    FontFile = pygame.font.SysFont(Font, Size)
    TextSurface = FontFile.render(Text, True, Colour)
    Surface.blit(TextSurface, Position)

def TextWrapped(Surface: pygame.Surface, Text: str, Font: pygame.font.Font, Colour: pygame.Color, Area: pygame.Rect):
    y = Area.top
    LineSpacing = -2

    # get the height of the font
    FontHeight = Font.size("Tg")[1]

    while Text:
        i = 1

        # determine if the row of text will be outside our area
        if y + FontHeight > Area.bottom:
            break

        # determine maximum width of line
        while Font.size(Text[:i])[0] < Area.width and i < len(Text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(Text): 
            i = Text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        TextSurface = Font.render(Text[:i], True, Colour) 

        Surface.blit(TextSurface, (Area.left, y))
        y += FontHeight + LineSpacing

        # remove the text we just blitted
        Text = Text[i:]

    return Text # Return any overflow text