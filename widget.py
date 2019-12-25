# base widget class

from utils import *
from node import *

class Widget(Node):
    def __init__(self, parent = None):
        super().__init__(parent)
        print("init widget")
        self.setColor(1, 0, 0)
        
    def setColor(self, r, g, b):
        self.color = Color(r, g, b) 
    
    def render(self):
        glColor(self.color.r, self.color.g, self.color.b)
        glPushMatrix()
        glTranslate(self.position.x, self.position.y, 0)
        rectangle(Vec2(0, 0), self.size)
        if self.children != None:
            for w in self.children:
                w.render()
        glPopMatrix()

