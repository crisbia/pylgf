# window manager class

import copy

from utils import *
from window import *

from OpenGL.GLUT import *

class Manager:
    def __init__(self):
        self._windows = []

    def createWindow(self, name):
        pass

    
class GLUTWindow(Window):
    def __init__(self, name):
        super().__init__(name)

        self.winId = glutCreateWindow(name)

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutMouseFunc(self.mouse)

    def setSize(self, w, h):
        super().setSize(w, h)

        glutSetWindow(self.winId)
        # todo : position
        glutPositionWindow(0,0)
        glutReshapeWindow(w, h)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glViewport(0, 0, self.size.x, self.size.y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.size.x, self.size.y, 0.0, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
        self.render()

        glutSwapBuffers()

    def mouse(self, button, state, x, y):
        print(button, state, x, y)

        event = MouseEvent()
        event.state.position = Vec2(x, y)
        event.state.leftButton = button == GLUT_LEFT_BUTTON and state == GLUT_DOWN
        event.state.middleButton = button == GLUT_MIDDLE_BUTTON and state == GLUT_DOWN
        event.state.rightButton = button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN
        wasHandled = self.handleEvent(event)
        print(f"Event handled: {wasHandled}")

        return None


class GLUTManager(Manager):
    def __init__(self):
        super().__init__()
        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) # | GLUT_BORDERLESS)
    
    def createWindow(self, name):
        w = GLUTWindow(name)
        self._windows.append(w)
        
        return w