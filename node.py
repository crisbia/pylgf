# base node class

from utils import *

class Node:
    def __init__(self, parent = None):
        self.parent = parent
        self.children = None
        self.inputHandlers = None
        self.transform = Transform(0, 0, 0)
        self.setSize(0, 0)
        self.z = 0
        self.name = "unnamed"
        if parent != None:
            parent.addChild(self)
    
    def addChild(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)

    def setPosition(self, x, y):
        if self.parent != None:
            self.transform.translation = Vec2(x, y)

    def setRotation(self, alfa):
        if self.parent != None:
            self.transform.rotation = Mat22(alfa)

    def setSize(self, w, h):
        self.size = Vec2(w, h)

    def getSize(self):
        return Vec2(self.size.x, self.size.y)

    def toGlobal(self, local):
        pos = self.transform.transformPoint(Vec2(local.x, local.y))
        p = self.parent
        while p != None:
            pos = p.transform.transformPoint(pos)
            p = p.parent
            
        return pos

    def toLocal(self, g):
        ancestors = []
        p = self
        while p != None:
            ancestors.insert(0, p)
            p = p.parent

        pos = Vec2(g.x, g.y)
        for p in ancestors:
            pos = p.transform.invTransformPoint(pos)

        return pos

    def render(self):
        if self.children != None:
            for w in sorted(self.children, key = lambda c: c.z):
                w.render()

    def handleEvent(self, event):
        # TODO logic to be defined but if a descendant handles this
        # stop trying
        if self.children != None:
            for child in sorted(self.children, key = lambda c: c.z, reverse = True):
                if child.handleEvent(event):
                    return True
        return False

class InputNode(Node):
    def __init__(self, parent = None):
        super().__init__(parent)