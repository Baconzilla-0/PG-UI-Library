import pygame
from pygame import Color, Rect, Vector2

import UILibrary
import UILibrary.Helpers as Helpers
import UILibrary.Style as Style

from UILibrary.Grid import *


pygame.init()

# Define the initial score
score = 0

# Define the initial score per click
score_per_click = 1

# Function to handle button clicks
def on_button_click():
    global score
    score += score_per_click
    ScoreDisplay.SetText(f"Score: {score}")


# Define the style sheet
Sheet = Style.Sheet()
Sheet.Entry(TargetClass="Any", State="Any").Set("Background", Color(255, 105, 180)).Set("Padding", Rect(5, 5, 5, 5)).Set("Margin", Rect(5, 5, 5, 5))  # Hot Pink
Sheet.Entry(TargetClass="Screen", State="Any").Set("Background", Color(135, 206, 250)).Set("Padding", Rect(0, 0, 0, 0)).Set("Margin", Rect(0, 0, 0, 0))  # Sky Blue
Sheet.Entry(TargetClass="List", State="Any").Set("Background", Color(240, 230, 140)).Set("Padding", Rect(0, 0, 0, 0)).Set("Margin", Rect(0, 0, 0, 0))  # Khaki
Sheet.Entry(TargetClass="Label", State="Any").Set("Background", Color(255, 160, 160)).Set("Padding", Rect(5, 5, 5, 5)).Set("Margin", Rect(0, 3, 0, 3))  # More Red

Sheet.Entry(TargetClass="TextButton", State="Idle").Set("Background", Color(144, 238, 144)).Set("Margin", Rect(5, 5, 5, 5))  # Light Green
Sheet.Entry(TargetClass="TextButton", State="Hover").Set("Background", Color(255, 255, 0)).Set("Margin", Rect(5, 5, 5, 5))  # Yellow
Sheet.Entry(TargetClass="TextButton", State="Held").Set("Background", Color(255, 69, 0)).Set("Margin", Rect(5, 5, 5, 5))  # Red-Orange

# Define the initial text size
Text = 0.6

# Define the initial window size
Start_Size = pygame.Vector2(350, 500)

# Create the main window
Window = UILibrary.Window.Main(Sheet, "Clicker Game", Start_Size, Vector2(100, 100), Icon=Helpers.GetFile(__file__, "assets/mouse.jpg"))

# Create the screen
Screen = UILibrary.Widgets.Screen(Sheet)
Window.SetScreen(Screen)

Main = UILibrary.Widgets.List(Screen).Scale(Divisions.WW).Dock(Compass.C)

Container = UILibrary.Widgets.List(Main).Scale(Divisions.WT)

Info = UILibrary.Widgets.List(Container).Scale(Divisions.HW).Dock(Compass.W) 
FunnyImage = UILibrary.Widgets.Image(Container, Helpers.GetFile(__file__, "assets/mouse.jpg")).Dock(Compass.E).Scale(Divisions.HW)

# Create a display for the score
ScoreDisplay = UILibrary.Widgets.Label(Info, f"Score: {score}", Text).Dock(Compass.N).Scale(Divisions.WT)
IncrementDisplay = UILibrary.Widgets.Label(Info, f"Go Up: {score}", Text).Dock(Compass.N).Scale(Divisions.WT)

# Create a button and set its callback
ClickButton = UILibrary.Widgets.TextButton(Info, "Click Me!", Text).Dock(Compass.S).Scale(Divisions.WT)
ClickButton.SetCallback(on_button_click)


# Define the upgrade costs and their effects with whimsical names
upgrades = [
    {"label": "Epic Thingamajig", "cost": 10, "increment": 1, "count": 0},
    {"label": "Silly Slapper", "cost": 50, "increment": 5, "count": 0},
    {"label": "Gunk Gadget", "cost": 100, "increment": 10, "count": 0},
    {"label": "Whimsical Widget", "cost": 200, "increment": 20, "count": 0},
    {"label": "Fantastical Feature", "cost": 500, "increment": 50, "count": 0},
    {"label": "Magical Mechanism", "cost": 1000, "increment": 100, "count": 0},
    {"label": "Ludicrous Lever", "cost": 2000, "increment": 200, "count": 0},
    {"label": "Absurd Apparatus", "cost": 5000, "increment": 500, "count": 0},
]

# Create a container for the upgrade buttons
UpgradeContainer = UILibrary.Widgets.ScrollList(Main).Dock(Compass.S).Fill(Constraints.H)

# Function to handle upgrade purchases
def on_upgrade_click(upgrade):
    global score, score_per_click
    if score >= upgrade["cost"]:
        score -= upgrade["cost"]
        score_per_click += upgrade["increment"]
        upgrade["count"] += 1
        IncrementDisplay.SetText(f"Go Up: {score_per_click}")
        ScoreDisplay.SetText(f"Score: {score}")
        update_upgrade_buttons()

# Function to update the text of upgrade buttons
def update_upgrade_buttons():
    for button, upgrade in zip(UpgradeButtons, upgrades):
        button.SetText(f"{upgrade['label']} ({upgrade['cost']} points) - {upgrade['count']} owned")

# Create upgrade buttons and set their callbacks
UpgradeButtons = []
for upgrade in upgrades:
    UpgradeButton = UILibrary.Widgets.TextButton(UpgradeContainer, f"{upgrade['label']} ({upgrade['cost']} points) - {upgrade['count']} owned", 0.3).Scale(Divisions.WQ)
    UpgradeButton.SetCallback(lambda u=upgrade: on_upgrade_click(u))
    UpgradeButtons.append(UpgradeButton)

Window.Loop()
