'''
Data structures for vector data.
'''

import numpy as np

class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def up():
        return Vector(0,0,1)

    @staticmethod
    def down():
        return Vector(0,0,-1)

    @staticmethod
    def left():
        return Vector(-1,0,0)

    @staticmethod
    def right():
        return Vector(1,0,0)

    @staticmethod
    def forward():
        return Vector(0,1,0)

    @staticmethod
    def back():
        return Vector(0,-1,0)

    def __add__(self, other):
        if isinstance(other, (float,int)):
            return Vector(self.x + other, self.y + other, self.z + other)
        elif isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, (float,int)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other):
        return self.__mul__(other)

    def array(self):
        return [self.x,self.y,self.z]

    def cross(self, vec):
        cross = np.cross(self.array(), vec.array())
        return Vector(*cross)

