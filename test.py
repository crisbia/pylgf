import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from panel import *

from window import *
from widget import *
from canvas import *
from inputhandler import *
from manager import *
from text import *
from fontmanager import *

#import freetype
#face = freetype.Face(r"C:\Windows\fonts\Arial.ttf")
#face.set_char_size( 48*64 )
#face.load_char('S')
#bitmap = face.glyph.bitmap
#print(bitmap.buffer)

def main():

    width = 800
    height = 600

    manager = GLUTManager()

    # Main widget. It will be a window eventually (no parent)
    w = manager.createWindow("pylgf")
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

    mh2 = MouseInputNode(can)
    mh2.name = "mh2"
    mh2.onPressed = lambda state: can.lineTo(state.position)

    mh = MouseInputNode(c1_2)
    mh.name = "mh"
    s = c1_2.getSize()
    mh.setSize(s.x, s.y)
    mh.onPressed = lambda state: c1_2.setColor(0, 0, 1)
    mh.onReleased = lambda state: c1_2.setColor(0, 1, 0)

    textBox = Widget(w)
    textBox.name = "textBox"
    textBox.setColor(1, 1, 1)
    textBox.setSize(200, 75)
    textBox.setPosition(100, 250)

    t = Text(textBox)
    t.text = "Here!!!"
    t.font = FontManager().getFont("Arial")

    # We are using the glut manager, we need to start the event loop
    glutMainLoop()


if __name__ == "__main__":
    # execute only if run as a script
    main()