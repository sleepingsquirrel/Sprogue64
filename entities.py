from math import sin, cos

class entity:
    def __init__(self, sprite, x, y, w, h, radius):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def show(self, rot):
        pass

    def move(self, v, dir):
        self.x += cos(dir) * v
        self.y += sin(dir) * v
