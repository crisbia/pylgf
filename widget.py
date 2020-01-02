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