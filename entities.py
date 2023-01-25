from math import sin, cos, atan, dist
import player

class entity:
    def __init__(self, sprite, x, y, w, h, hp=100):
        self.sprite = open(sprite)
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

    def update(self, target):
        dir = atan(self.y - target.y, self.x - target.x)
        self.move(0.04, dir)
        if dist([target.x, target.y], [self.x, self.y]) < self.w + target.w:
            return True
        return False
