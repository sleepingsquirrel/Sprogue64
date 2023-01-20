from math import sin, cos

class entity:
    def __init__(self, sprite, x, y, w, h, hp=100):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
    
    def show(self, rot):
        pass

    def move(self, v, dir):
        self.x += cos(dir) * v
        self.y += sin(dir) * v
