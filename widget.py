# base widget class

from utils import *
from node import *

class Widget(Node):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setColor(1, 0, 0)
        
    def setColor(self, r, g, b):
        self.color = Color(r, g, b) 
    
    def render(self):
        glColor(self.color.r, self.color.g, self.color.b)
        #glPushMatrix()
        #glTranslate(self.transform.translation.x, self.transform.translation.y, 0)
        # glRotate(self.rotation, 0, 0, 1)
        #p1 = self.transform.transform(Vec2(0, 0))
        #p2 = self.transform.transform(Vec2(self.size.x, 0))
        #p3 = self.transform.transform(Vec2(self.size.x, self.size.y))
        #p4 = self.transform.transform(Vec2(0, self.size.y))
        p1 = self.toGlobal(Vec2(0, 0))
        p2 = self.toGlobal(Vec2(self.size.x, 0))
        p3 = self.toGlobal(Vec2(self.size.x, self.size.y))
        p4 = self.toGlobal(Vec2(0, self.size.y))
        lgf_rectangle(p1, p2, p3, p4)
        if self.children != None:
            for w in self.children:
                w.render()
        #glPopMatrix()

