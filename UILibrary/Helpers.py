import pygame

Cache = {}

import sys, os

def GetFile(Start, File: str):
    if getattr(sys, 'frozen', False):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(os.path.abspath(Start))
    return basedir + "/" + File

def Box(Widget, Colour, Border = None, Rect = None):
    if Border == None:
        Border = Widget.Theme.BorderColour

    #Rect = Widget.Surface.get_rect()
    if Rect == None:
        if Widget.Theme.Absolute:
            Rect = Widget.Rect
        else:
            Rect = Widget.MarginRect

    pygame.draw.rect(Widget.Surface, Colour, Rect, 0, Widget.Theme.BorderRadius)
    pygame.draw.rect(Widget.Surface, Border, Rect, Widget.Theme.BorderWidth, Widget.Theme.BorderRadius)


def Text(Surface: pygame.Surface, Text: str, Font: str, Colour: pygame.Color, Position: pygame.Vector2, Area = None): # A function to render text with a specified size, font, and position
    if Area == None:
        Area = Surface.get_size()

    px = (Area[1] - Position[1]) * ( 72 / 96 ) 
    
    try:
        FontFile = Cache[Font][int(px)]
    except:
        FontFile = pygame.font.Font(Font, int(px))
        try:
            Cache[Font][str(int(px))] = FontFile
        except:
            Cache[Font] = {}
            Cache[Font][str(int(px))] = FontFile

    Width = 0
    for Char in Text:
        Individual = FontFile.size(Char)[0]
        Width += Individual

    Scale =  px / Width
    
    Goal = Area[0] - (Position[0] * 2)
    if Width > Goal:
        try:
            FontFile = Cache[Font][str(int(Scale * Goal))]
        except:
            FontFile = pygame.font.Font(Font, int(Scale * Goal))
            Cache[Font][str(int(Scale * Goal))] = FontFile
        #FontFile = pygame.font.Font(Font, int(Scale * Goal))
        #Cache[Font][int(Scale * Goal)]

    TextSurface = FontFile.render(Text, True, Colour)
    Surface.blit(TextSurface, Position)


def blit_text(Surface: pygame.Surface, Text: str, Pos, Font: pygame.font.Font, Colour: pygame.Color, Area: pygame.Rect):

    words = [word.split(' ') for word in Text.splitlines()]  # 2D array where each row is a list of words.
    space = Font.size(' ')[0]  # The width of a space.
    max_width, max_height = Area.width, Area.height
    x, y = Pos
    for line in words:
        for word in line:
            word_surface = Font.render(word, True, Colour)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = Pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            Surface.blit(word_surface, (x + Area.left, y + Area.top))
            x += word_width + space
        x = Pos[0]  # Reset the x.
        y += word_height  # Start on new row.

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