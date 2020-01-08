# window manager class

import copy

from utils import *
from window import *

class Manager:
    def __init__(self):
        self._windows = []
        pass

    def createWindow(self, name):
        pass

    
class GLUTWindow(Window):
    def __init__(self, name):
        super().__init__(name)

class GLUTManager(Manager):
    def __init__(self):
        super().__init__()
    
    def createWindow(self, name):
        w = GLUTWindow(name)
        self._windows.append(w)
        return w
