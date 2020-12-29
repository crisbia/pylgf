import sys
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

from panel import *

from window import *
from widget import *
from canvas import *
from inputhandler import *
from manager import *
from text import *
from fontmanager import *

def main():

    width = 300
    height = 300

    manager = GLFWManager()

    # Main widget. It will be a window eventually (no parent)
    w = manager.createWindow("pylgf", width, height)
    #w.setSize(width, height)
    #w.setColor(0.7, 0.7, 0.7)
    w.setColor(0, 1, 0)

    c1 = Widget(w)
    c1.name = "c1"
    c1.setPosition(0, 0)
    c1.setSize(150, 300)
    c1.setColor(1, 0.7, 0.7)

    manager.startLoop()


if __name__ == "__main__":
    # execute only if run as a script
    main()