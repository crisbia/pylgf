# window class

import copy

from utils import *
from node import *
from widget import *

class Window(Widget):
    def __init__(self, name):
        super().__init__(None)
        self.name = name