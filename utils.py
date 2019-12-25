from OpenGL.GL import *

def rectangle(pos, size):
    width = size.x
    height = size.y
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(pos.x, pos.y) # Coordinates for the bottom left point
    glVertex2f(pos.x + width, pos.y) # Coordinates for the bottom right point
    glVertex2f(pos.x + width, pos.y + height) # Coordinates for the top right point
    glVertex2f(pos.x, pos.y + height) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)