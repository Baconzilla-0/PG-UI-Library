import pygame
from pygame import Vector2, Color, Rect

from .. import Helpers

from ..Grid import *
from ..Style import Theme


class Widget:
    def __init__(self, Parent, Position = Vector2(0, 0), Size = Vector2(100, 100), Name = "Widget"):
        ## Rendering Setup
        self.Position = Position
        self.AbsolutePosition = Position
        self.Size = Size
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.Surface = pygame.Surface(self.Size, pygame.SRCALPHA)

        self._Changed = False

        ## Style Setup
        self._Name = Name
        self._State = "Idle"
        self.Style = None
        self.Theme = Theme()
        self._Visible = True
        self._Absolute = False # if true widget ignores its margin
        self._Transparent = True
        self._Render = True

        ## Scaling & Resizing
        self.Scaled = None
        self.Docked = None
        self.Filled = None
        self.Aspect = None

        ## Interactivity
        self.Interactive = False
        self.Hovered = False
        self.Focused = False
        self.Clicked = False
        self.Holding = False
        self.RelativeMouse = pygame.Vector2(0, 0)
        self.MouseStart = pygame.Vector2(0, 0)
        self.Callback = None

        ## Final Setup
        self.Root = False
        self.Parent = None
        self.ZIndex = 0
        self.Children = []
        self.SetParent(Parent)
        

        self.PaddingRect = pygame.Rect(0, 0, self.Size.x, self.Size.y)
  
    def __str__(self):
        Output = f"""
        ZIndex: {self.ZIndex}
        Position: {self.Position}
        Size: {self.Size}
        """
        return Output
    
    ## Property Methods
    def Absolute(self):
        self._Absolute = True

        return self

    def Name(self, Name):
        self._Name = Name

        return self

    def Dock(self, Alignment: Alignment):
        Alignment.Apply(self)
        self.Docked = Alignment

        return self
    
    def Constrain(self, Aspect: Aspect):
        Aspect.Apply(self)
        self.Aspect = Aspect

        return self

    def Scale(self, Scale: Scale):
        Scale.Apply(self)
        self.Scaled = Scale

        return self
    
    def Fill(self, Fill: Fill):
        Fill.Apply(self)
        self.Filled = Fill

        return self

    ## Setters
    def SetParent(self, Parent):
        if self.Parent != None:
            self.Parent.Children.remove(self)

        if Parent != None:
            self.Parent = Parent
            if self.Parent.Style != None:
                self.Style = Parent.Style
                self.Style.Apply(self)

                self.Generate()

            self.Surface = Parent.Surface

        if Parent == None:
            self.ZIndex = 1
        else:
            self.ZIndex = Parent.ZIndex + 1
            Parent.Children.append(self)

    def SetCallback(self, Callback):
        self.Callback = Callback

    def SetState(self, State):
        #if self._State != State:
            #self._Changed = True
        self._State = State

    def SetSize(self, Size):
        if self.Size != Size:
            self._Changed = True
        self.Size = Size
        
    def SetPosition(self, Position):
        if self.Position != Position:
            self._Changed = True
        self.Position = Position

    ## Getters
    def GetRoot(self):
        if self.Root:
            return self
        else:
            return self.Parent.GetRoot()

    def Clear(self):
        for Child in self.Children:
            del Child
        self.Children = []

    ## Update Methods
    def Changed(self):
        print("I AM UPDATE")
        self.Generate()

    # Updates the margin and padding, as well as caching them for efficiency
    def Generate(self):
        self.Style = self.Parent.Style
        self.Style.Apply(self)

        self.MarginRect = pygame.Rect(
            0, 
            0, 
            self.Size.x - self.Theme.Margin.width - self.Theme.Margin.left, 
            self.Size.y - self.Theme.Margin.height - self.Theme.Margin.top
        )

        self.PaddingRect = pygame.Rect(
            self.MarginRect.left + self.Theme.Padding.left, 
            self.MarginRect.top + self.Theme.Padding.top, 
            self.MarginRect.width - self.Theme.Padding.width, 
            self.MarginRect.height - self.Theme.Padding.height
        )

        if self._Absolute:
            self.PaddingRect = pygame.Rect(0, 0, self.Size.x, self.Size.y)

        for Child in self.Children:
            Child: Widget
            Child.Generate()

    # this runs Pre-Update and is responsible for all interaction and the box drawing.
    def Evaluate(self):
        ## Applys state specific styling.
        self.Style.Apply(self)
        if self._Render == True:
            Helpers.Box(self, self.Theme.Background) # draws the widget according to the stylesheet

        
        if self._Absolute:
            self.AbsolutePosition = self.Position + self.Parent.AbsolutePosition
        else:
            self.AbsolutePosition = self.Position + self.Parent.AbsolutePosition + self.Theme.Margin.center

        PhysicalRect = pygame.Rect(self.AbsolutePosition, self.PaddingRect.size)
        MousePos = self.GetRoot().Inputs.MousePosition
        self.RelativeMouse = pygame.Vector2(MousePos) - pygame.Vector2(self.AbsolutePosition)

        # If the widget does not require interation, stop the evaluation.
        if not self.Interactive:
            return

        ## Hover Detection
        if PhysicalRect.collidepoint(MousePos):
            self.Hovered = True
            self.SetState("Hover")
        else:
            self.Hovered = False
            self.SetState("Idle")
        
        ## Focus & Click Detection
        if self.Clicked:
            self.Clicked = False

        if self.GetRoot().Inputs.Mouse1:
            if self.Hovered:
                if not self.Holding:
                    self.MouseStart = pygame.Vector2(MousePos) - pygame.Vector2(self.AbsolutePosition)

                self.Focused = True
                self.Holding = True
                self.SetState("Held")
            else:

                self.Focused = False
        else:
            if self.Hovered and self.Holding:
                self.Clicked = True

            
            self.Holding = False
            if not self.Hovered:
                self.SetState("Idle")

    # updates all children then blits to its parent
    def Update(self):
        ## Hello my name is responsive layout
        if self.Scaled:
            self.Scale(self.Scaled)
        if self.Docked:
            self.Dock(self.Docked)
        if self.Filled:
            self.Fill(self.Filled)
        if self.Aspect:
            self.Constrain(self.Aspect)

        ## Update Children
        for Child in self.Children:
            Child: Widget
            
            Child.Evaluate()
            Child.Update()

        ## Update Self
        self.Rect = pygame.Rect(pygame.Vector2(0, 0), self.Size)
        self.Size = pygame.Vector2(self.Size)

        if self._Changed:
            self.Changed()
            self._Changed = False

        if self._Transparent:
            ## transparency workaround because pygame is mean
            self.Surface.set_colorkey(pygame.Color(255, 0, 255))

        if self._Visible:
            if self._Absolute:
                self.Parent.Surface.blit(self.Surface.convert_alpha(), self.Position, self.Rect)
            else:
                self.Parent.Surface.blit(self.Surface.convert_alpha(), self.Position + self.Theme.Margin.topleft)
        try:
            # recreate surface to reflect size changes (for responsive layouts)
            if self._Absolute:
                self.Surface = pygame.Surface(self.Size, pygame.SRCALPHA)
            else:
                self.Surface = pygame.Surface(self.MarginRect.size, pygame.SRCALPHA) 
        except:
            pass
    