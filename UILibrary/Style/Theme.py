from pygame import Rect, Color

class Theme:
    def __init__(self, a=None):#  | "Hover" | "Hold"
        self.Background = Color(160, 160, 160)
        self.Foreground = Color(15, 15, 15)
        
        self.Padding = Rect(5, 5, 5, 5)
        self.Margin = Rect(10, 10, 10, 10)

        self.BorderColour = Color(120, 120, 120)
        self.BorderWidth = 2
        self.BorderRadius = -1 #6

        self.Font = None