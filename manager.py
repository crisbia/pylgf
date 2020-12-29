# window manager class

import copy

from utils import *
from window import *

from OpenGL.GLUT import *

import glfw
from glfw.GLFW import *

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
        glutReshapeFunc(self.reshape)

#    def setSize(self, w, h):
#        super().setSize(w, h)
#        #glutSetWindow(self.winId)
#        # todo : position
#        #glutPositionWindow(0,0)
#        #glutReshapeWindow(w, h)

    def display(self):
        glutSetWindow(self.winId)
        w = glutGet(GLUT_WINDOW_WIDTH)
        h = glutGet(GLUT_WINDOW_HEIGHT)
        if w != self.size.x or h != self.size.y:
            glutReshapeWindow(w, h)
            glutPostRedisplay()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glViewport(0, 0, self.size.x, self.size.y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.size.x, self.size.y, 0.0, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
        self.render()

        glutSwapBuffers()

    def reshape(self, w, h):
        pass

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


class GLFWWindow(Window):
    def __init__(self, name, width, height):
        super().__init__(name)

        #cs = glfw.get_window_content_scale()
        #self.win = glfw.create_window(int(width / 2), int(height / 2), name, None, None)
        self.win = glfw.create_window(width, height, name, None, None)
        super().setSize(width, height)
        ws = glfw.get_window_size(self.win)
        pass
        
    def setSize(self, w, h):
        super().setSize(w, h)
        #glutSetWindow(self.winId)
        # todo : position
        glfw.set_window_size(self.win, int(w / 2), int(h / 2))

    def render(self):

        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        fs = glfw.get_framebuffer_size(self.win)
        glViewport(0, 0, fs[0], fs[1])
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.size.x, self.size.y, 0.0, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
        super().render()

class GLFWManager(Manager):
    def __init__(self):
        super().__init__()
        glfw.init()
    
    def createWindow(self, name, width, height):
        w = GLFWWindow(name, width, height)
        self._windows.append(w)
        
        return w

    def startLoop(self):
        while len(self._windows) > 0:
            active_windows = []
            for w in self._windows:
                if glfw.window_should_close(w.win):
                    glfw.destroy_window(w.win)
                else:
                    active_windows.append(w)

                self._windows = active_windows                

            for w in self._windows:
                # Make the window's context current
                glfw.make_context_current(w.win)
    
                # Render here, e.g. using pyOpenGL
                #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                #glClearColor(1, 0, 0, 1)
                w.render()

                # Swap front and back buffers
                glfw.swap_buffers(w.win)

            # Poll for and process events
            glfw.poll_events()

        glfw.terminate()