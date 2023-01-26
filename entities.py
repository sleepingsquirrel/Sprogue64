from math import sin, cos, atan, dist
import player
from PIL import Image
import os
import numpy as np
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


class texture_atlas:
    def __init__(self,loc):
        
        # texlen = 0
        # for i, filename in enumerate(os.listdir(loc + "/")):
        #     if "." in filename:
        #         texlen += 1
        # assert texlen > 0
        # self.atlas = np.zeros((1000*texlen,1000,4), "int8")
        # for i, filename in enumerate(os.listdir(loc + "/")):
        #     with Image.open(loc + "/" + filename) as img:
        #         assert img.size[0] == 1000
        #         assert img.size[1] == 1000
        #         for y in range(1000):
        #             if not y % 10:
        #                 print(y)
        #             self.atlas[1000*i:1000*i+1000,y] = np.array(img.getdata())[y*1000:y*1000+1000]

        image = Image.fromarray(self.atlas)
        image.show()

        