# canvas class

import copy

from utils import *
from node import *
from inputhandler import *

class Canvas(Node):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.points = []
            
    def render(self):
        globalPoints = []
        for p in self.points:
            globalPoints.append(p)#self.toGlobal(p))
        glColor(0, 0, 1)
        glPointSize(5)
        lgf_points(globalPoints)
        super().render()