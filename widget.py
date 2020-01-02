# base widget class

import copy

from utils import *
from node import *
from inputhandler import *

class Widget(Node):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setColor(1, 0, 0)
        
    def setColor(self, r, g, b):
        self.color = Color(r, g, b) 
    
    def render(self):
        glColor(self.color.r, self.color.g, self.color.b)
        p1 = self.toGlobal(Vec2(0, 0))
        p2 = self.toGlobal(Vec2(0, self.size.y))
        p3 = self.toGlobal(Vec2(self.size.x, self.size.y))
        p4 = self.toGlobal(Vec2(self.size.x, 0))
        lgf_rectangle(p1, p2, p3, p4)
        super().render()

class MouseInputNode(InputNode):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.state = MouseState()
        # by default, size it as the parent.
        if parent != None:
            self.size = copy.deepcopy(parent.size)

    def onPressed(self, state):
        pass

    def onReleased(self, state):
        pass

    def handleEvent(self, event):
        # if the event is handled by one of the children
        # just move on
        if super().handleEvent(event):
            return True

        # handle only mouse events
        if type(event) != MouseEvent:
            return False

        # convert the event to coordinates local to the node
        localPos = self.toLocal(event.state.position)
        if localPos.x < 0 or localPos.y < 0 or localPos.x > self.size.x or localPos.y > self.size.y:
            return False

        if (event.state.leftButton and not self.state.leftButton) or \
            (event.state.middleButton and not self.state.middleButton) or \
            (event.state.rightButton and not self.state.rightButton):
            self.onPressed(copy.deepcopy(event.state))

        if (not event.state.leftButton and self.state.leftButton) or \
            (not event.state.middleButton and self.state.middleButton) or \
            (not event.state.rightButton and self.state.rightButton):
            self.onReleased(copy.deepcopy(event.state))

        self.state = copy.deepcopy(event.state)
        # position is in node's coordinate
        self.state.position = copy.deepcopy(localPos)
        return True
