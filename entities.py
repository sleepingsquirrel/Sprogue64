from math import sin, cos, atan, dist
import player
from pil import Image
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
        
        for i, filename in enumerate(os.listdir("assets/")):
            if "." in filename:
                if filename.split('.')[1] == "gsm":
                    texlen += 1
        self.atlas = numpy.zeros(1000*texlen,1000,4)
        for i, filename in enumerate(os.listdir("assets/")):
            with Image.open("assets/" + filename) as img:
                pix = img.load()
                assert img.size[0] == 1000
                assert img.size[1] == 1000
                self.atlas[1000*i:1000*i+1000,0:1000] = pix

        
