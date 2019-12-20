# base widget class

from utils import *

class Widget:
    def __init__(self, parent = None):
        self.children = None
        print("init widget")
        self.setPosition(100, 100)
        self.setSize(100, 100)
        self.setColor(1, 0, 0)
        if parent != None:
            parent.addChild(self)
        
    def setColor(self, r, g, b):
        self.color = Color(r, g, b) 
    
    def setPosition(self, x, y):
        self.position = Vec2(x, y)

    def setSize(self, w, h):
        self.size = Vec2(w, h)

    def render(self):
        glColor(self.color.r, self.color.g, self.color.b)
        square(self.position, self.size)
        if self.children != None:
            for w in self.children: w.render()

    def addChild(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)

