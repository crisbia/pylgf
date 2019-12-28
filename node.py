# base node class

from utils import *

class Node:
    def __init__(self, parent = None):
        self.parent = parent
        self.children = None
        self.transform = Transform(0, 100, 100)
        self.setSize(100, 100)
        if parent != None:
            parent.addChild(self)
    
    def addChild(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)

    def setPosition(self, x, y):
        self.transform.translation = Vec2(x, y)

    def setRotation(self, alfa):
        self.transform.rotation = Mat22(alfa)

    def setSize(self, w, h):
        self.size = Vec2(w, h)

    def __toGlobal__(self, local):
        pos = Vec2(local.x, local.y)
        p = self.parent
        while p != None:
            pos = pos + p.position
            p = p.parent
        return pos

    # Position is always relative to the parent
    def getGlobalPosition(self):
        return self.__toGlobal__(self.position)