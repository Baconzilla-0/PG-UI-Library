from pygame import Color, Rect

#from .. import Widgets
import copy

class Entry:
    def __init__(self, TargetName: str = None, TargetClass: str = None, State: bool = "Idle"):#  | "Hover" | "Hold"
        self.TargetName = TargetName
        self.TargetClass = TargetClass
        self.State = State


        self.Background = Color(160, 160, 160)
        self.Foreground = Color(15, 15, 15)
        
        self.Padding = Rect(5, 5, 5, 5)
        self.Margin = Rect(10, 10, 10, 10)

        self.BorderColour = Color(120, 120, 120)
        self.BorderWidth = 2
        self.BorderRadius = 6

        self.Font = None

    def Set(self, Attribute, Value):
        self.__setattr__(Attribute, Value)

        return self

    def From(Entry):
        return copy.deepcopy(Entry)

    def Apply(self, Widget):
        Name = Widget.__class__.__name__

        if Widget.Name == self.TargetName or Name == self.TargetClass:
            if self.State == "Any":
                Widget.Theme = self
            elif Widget.State == self.State:
                Widget.Theme = self
        if Widget.Theme == None:
            if self.TargetClass == "Any":
                if self.State == "Any":
                    Widget.Theme = self
                elif Widget.State == self.State:
                    Widget.Theme = self