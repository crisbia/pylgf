from utils import *

class Event:
    def __init__(self):
        pass

class MouseEvent(Event):
    def __init__(self):
        super().__init__()
        self.state = MouseState()

class MouseState:
    def __init__(self):
        self.position = Vec2(0, 0)
        self.leftButton = False
        self.middleButton = False
        self.rightButton = False