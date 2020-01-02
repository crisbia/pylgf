# canvas class

import copy

from utils import *
from node import *
from inputhandler import *

class PolyLine:
    def __init__(self):
        self.points = []
        self.color = Color(1, 0, 0)

    def addPoint(self, point):
        self.points.append(copy.deepcopy(point))

class Canvas(Node):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.currentLine = None
        self.lines = []
        self.currentPos = Vec2(0, 0)

    def moveTo(self, pos):
        self.currentPos = copy.deepcopy(pos)
        self.__startLine(pos)

    def __startLine(self, point):
        if self.currentLine == None:
            self.currentLine = PolyLine()
            self.currentLine.addPoint(point)

    def __endLine(self):
        if self.currentLine != None:
            # move the line to the list
            self.lines.append(self.currentLine)
            self.currentLine = None
    
    def lineTo(self, point):
        if self.currentLine == None:
            return
        self.currentLine.addPoint(point)

    # add a dot in place
    def dot(self):
        pass

    def render(self):
        glColor(0, 0, 1)
        glLineWidth(2)
        if self.currentLine != None:
            lgf_line(self.currentLine.points)
        for l in self.lines:
            lgf_line(l.points)

        #glPointSize(5)
        #lgf_points(self.points)
        super().render()