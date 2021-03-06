from OpenGL.GL import *
import math

def lgf_quad(p1, p2, p3, p4):
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS)
    glVertex2f(p1.x, p1.y) # Coordinates for the bottom left point
    glVertex2f(p2.x, p2.y) # Coordinates for the bottom right point
    glVertex2f(p3.x, p3.y) # Coordinates for the top right point
    glVertex2f(p4.x, p4.y) # Coordinates for the top left point
    glEnd()

def lgf_points(points):
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p.x, p.y)
    glEnd()

def lgf_polyline(points):
    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex2f(p.x, p.y)
    glEnd()

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

class Mat22:
    def __init__(self, angle):
        c = math.cos(angle)
        s = math.sin(angle)
        self.col1 = Vec2(c, s)
        self.col2 = Vec2(-s, c)

    def mult(self, v):
        return Vec2(
            self.col1.x * v.x + self.col2.x * v.y, 
            self.col1.y * v.x + self.col2.y * v.y)

    def transpose(self):
        t = Mat22(0)
        t.col1.x =  self.col1.x
        t.col1.y =  self.col2.x
        t.col2.x =  self.col1.y
        t.col2.y =  self.col2.y
        return t


class Transform:
    def __init__(self, a, x, y):
        self.rotation = Mat22(a)
        self.translation = Vec2(x, y)

    def transformPoint(self, v):
        return self.rotation.mult(v) + self.translation

    def invTransformPoint(self, v):
        return self.rotation.transpose().mult(v - self.translation)

    def inverse(self):
        t = Transform(0, 0, 0)
        t.rotation = self.rotation.transpose()
        t.translation = Vec2(-self.translation.x, -self.translation.y)
        return t

class Context:
    __shared_state = {}

    pos = Vec2(0, 0)

    def __init__(self):
        self.__dict__ = self.__shared_state

    def setPos(self, x, y):
        self.pos.x = x
        self.pos.y = y
