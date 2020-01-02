import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from panel import *

from widget import *
from inputhandler import *

width = 800
height = 600

# Main widget. It will be a window eventually (no parent)
w = Widget()
w.setSize(width, height)
w.setColor(0.7, 0.7, 0.7)

c1 = Widget(w)
c1.setPosition(20, 50)
c1.setSize(300, 300)
c1.setColor(1, 0.7, 0.7)
#c1.setRotation(math.pi / 64)

c1_1 = Widget(c1)
c1_1.setSize(100, 100)
c1_1.setPosition(50, 50)

MyHandler = type("MyHandler", 
              (), 
              {"handle": lambda self, event: "Handled event!"})

c1_2 = Widget(c1)
c1_2.setSize(150, 80)
c1_2.setPosition(70, 50)
c1_2.setRotation(-math.pi / 6)
c1_2.setColor(0, 1, 0)
c1_2.z = -1

mh1 = MouseInputNode(c1_1)

def testMousePress(state):
    print("press called!!!")
    c1_2.setColor(0, 0, 1)

def testMouseRelease(state):
    print("release called!!!")
    c1_2.setColor(0, 1, 0)

mh = MouseInputNode(c1_2)
s = c1_2.getSize()
mh.setSize(s.x, s.y)
mh.onPressed = testMousePress
mh.onReleased = testMouseRelease


def mouse(button, state, x, y):
    print(button, state, x, y)

    event = MouseEvent()
    event.state.position = Vec2(x, y)
    event.state.leftButton = button == GLUT_LEFT_BUTTON and state == GLUT_DOWN
    event.state.middleButton = button == GLUT_MIDDLE_BUTTON and state == GLUT_DOWN
    event.state.rightButton = button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN
    print(f"Event handled: {w.handleEvent(event)}")

    return None

# The display() method does all the work; it has to call the appropriate
# OpenGL functions to actually display something.
def display():
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, height, 0.0, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

    # ... render stuff in here ...
    # It will go to an off-screen frame buffer.
    glLoadIdentity()

    w.render()

    # Copy the off-screen buffer to the screen.
    glutSwapBuffers()

glutInit(sys.argv)

# Create a double-buffer RGBA window.   (Single-buffering is possible.
# So is creating an index-mode window.)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Create a window, setting its title
glutCreateWindow('interactive')
glutPositionWindow(0,0)
glutReshapeWindow(width, height)

# Set the display callback.  You can set other callbacks for keyboard and
# mouse events.
glutDisplayFunc(display)

glutIdleFunc(display)

glutMouseFunc(mouse)

# Run the GLUT main loop until the user closes the window.
glutMainLoop()