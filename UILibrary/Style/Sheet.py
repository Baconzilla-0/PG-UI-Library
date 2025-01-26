from .Entry import Entry as E
from .. import Widgets

class Sheet:
    def __init__(self):
        self.Entries = []

    def Add(self, Entry: E):
        self.Entries.append(Entry)

    def Entry(self, TargetName: str = None, TargetClass: str = None, State: bool = "Idle"): #  | "Hover" | "Hold"
        Ent = E(TargetName, TargetClass, State)
        self.Add(Ent)
        return Ent


    def Apply(self, Widget: Widgets.Widget):
        for Index, Theme in enumerate(self.Entries):
            Theme: E
            Theme.Apply(Widget)