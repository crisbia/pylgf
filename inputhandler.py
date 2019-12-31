from utils import *

class InputHandler:
    # Return specific info on how the event was handled
    # or None if not handled
    def handle(self, event):
        return None

class Event:
    def __init__(self):
        print("init event")

class MouseEvent(Event):
    def __init__(self):
        super().__init__()
        self.position = Vec2(0, 0)

    def setPosition(self, x, y):
        self.position = Vec2(x, y)

    def getPosition(self):
        return Vec2(self.position.x, self.position.y)

class MouseInputHandler(InputHandler):
    def __init__(self, node):
        super().__init__()
        self.node = node # node to which this is attached

    def handle(self, event):
        return True