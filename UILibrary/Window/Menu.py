from ..Widget import Widget
from ..Widgets import TextButton


from pygame import Vector2, Color

class Option:
    def __init__(self, Screen: Widget, Label: str, Callback=None, Children=None):
        self.Label = Label
        self.Screen = Screen
        self.Children = Children if Children is not None else []
        self.Open = False

        self.Button = TextButton(Screen, Label, 0.5, self.toggle_dropdown)

        if Callback is not None:
            self.Callback = Callback
        else:
            self.Menu = Dropdown(Screen, None, Vector2(0, 0))

    def toggle_dropdown(self):
        self.Open = not self.Open
        if self.Open:
            self.Menu.show()
        else:
            self.Menu.hide()

class Dropdown(Widget):
    def __init__(self, Parent, Theme, Position: Vector2):
        super().__init__(Parent, Theme, Position, Vector2(10, 10))

        self.Options = []
        self.Visible = False

    def AddOption(self, option: Option):
        option.Screen = self.Parent
        self.Options.append(option)

    def show(self):
        self.Visible = True
        #for option in self.Options:
        #    option.Button.show()

    def hide(self):
        self.Visible = False
        #for option in self.Options:
        #    option.Button.hide()