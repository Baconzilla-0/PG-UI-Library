import pygame
from pygame import Color, Rect, Vector2

import UILibrary
import UILibrary.Helpers as Helpers
import UILibrary.Style as Style
import UILibrary.Grid as Grid
from UILibrary.Grid import Compass, Constraints, Divisions

pygame.init()

Sheet = Style.Sheet()
Sheet.Entry(TargetClass="Any", State="Any").Set("Background", Color(140, 140, 140)).Set("Padding", Rect(5, 5, 5, 5)).Set("Margin", Rect(5,5,5,5))
Sheet.Entry(TargetClass="Screen", State="Any").Set("Background", Color(140, 140, 140)).Set("Padding", Rect(0, 0, 0, 0)).Set("Margin", Rect(0,0,0,0))

Sheet.Entry(TargetClass="TextButton", State="Idle").Set("Background", Color(160, 160, 160)).Set("Margin", Rect(5,5,5,5))
Sheet.Entry(TargetClass="TextButton", State="Hover").Set("Background", Color(180, 180, 180)).Set("Margin", Rect(5,5,5,5))
Sheet.Entry(TargetClass="TextButton", State="Held").Set("Background", Color(130, 130, 130)).Set("Margin", Rect(5,5,5,5))

Text = 0.6

Start_Size = pygame.Vector2(350, 500)
Window = UILibrary.Window.Main(Sheet, "Calculator", Start_Size, Vector2(100, 100), Icon = Helpers.GetFile(__file__, "assets/icon.jpg"))

Screen = UILibrary.Widgets.Screen(Sheet)
Window.SetScreen(Screen)

InputScale = UILibrary.Grid.Scale(Vector2(1, 1.2))

# Create a display for the calculator
Display = UILibrary.Widgets.Label(Screen, "0", Text).Dock(Compass.NW).Scale(Divisions.WF)
Image = UILibrary.Widgets.Image(Screen, Helpers.GetFile(__file__, "assets/icon.jpg")).Dock(Compass.NE).Scale(Divisions.FF)

# Create a container for the buttons
ButtonContainer = UILibrary.Widgets.List(Screen).Dock(Compass.S).Scale(InputScale)

# Define button labels
buttons = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', '(', ')', '+',
    ".", "C", "D", "="
]

# Function to handle button clicks
def on_button_click(label):
    current_text = Display.Text
    
    if label == '=':
        try:
            result = str(eval(current_text))
            Display.SetText(result)
           
        except Exception:
            Display.SetText("Error")
    elif label == 'C':
        Display.SetText("0")
    elif label == 'D':
        if len(current_text) > 1:
            Display.SetText(current_text[:-1])
        else:
            Display.SetText("0")
    else:
        if current_text == "0":
            Display.SetText(label)
        elif current_text == "Error":
            Display.SetText(label)
        else:
            Display.SetText(current_text + label)


# Create buttons and set their callbacks
for label in buttons:
    button = UILibrary.Widgets.TextButton(ButtonContainer, label, Text).Scale(Divisions.QF)
    button.SetCallback(lambda l=label: on_button_click(l))

# Start the UI loop
Window.Loop()