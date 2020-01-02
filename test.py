import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from panel import *

from widget import *
from canvas import *
from inputhandler import *

width = 800
height = 600

# Main widget. It will be a window eventually (no parent)
w = Widget()
w.name = "w"
w.setSize(width, height)
w.setColor(0.7, 0.7, 0.7)

c1 = Widget(w)
c1.name = "c1"
c1.setPosition(20, 50)
c1.setSize(300, 300)
c1.setColor(1, 0.7, 0.7)

c1_1 = Widget(c1)
c1_1.name = "c1_1"
c1_1.setSize(100, 100)
c1_1.setPosition(50, 50)

c1_2 = Widget(c1)
c1_2.name = "c1_2"
c1_2.setSize(150, 80)
c1_2.setPosition(70, 50)
c1_2.setRotation(-math.pi / 6)
c1_2.setColor(0, 1, 0)
c1_2.z = -1

can = Canvas(c1)
can.name = "can"
can.setSize(c1.getSize().x, c1.getSize().y)
can.moveTo(Vec2(200, 200))
can.z = -1

can.addPoint = lambda state: can.lineTo(state.position)

mh2 = MouseInputNode(can)
mh2.name = "mh2"
mh2.onPressed = can.addPoint

def testMousePress(state):
    c1_2.setColor(0, 0, 1)

def testMouseRelease(state):
    c1_2.setColor(0, 1, 0)

mh = MouseInputNode(c1_2)
mh.name = "mh"
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

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, height, 0.0, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

    glLoadIdentity()

    # Render the scene
    w.render()

    glutSwapBuffers()

glutInit(sys.argv)

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

glutCreateWindow('pylgf')
glutPositionWindow(0,0)
glutReshapeWindow(width, height)

glutDisplayFunc(display)

glutIdleFunc(display)

glutMouseFunc(mouse)

glutMainLoop()