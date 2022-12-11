import numpy as np

class wall:
    def __init__(self,wtype,rot,x,y,w,h):
        self.type = wtype
        self.rot = rot
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        


class world:
    def __init__(self):
        self.map = {}
        self.load_from_file()
    def get_chunk(self, x,y):
        if (x,y) in self.map:
            return self.map[(x,y)]
        else:
            return []

    def load_from_file(self):
        with open("world/world.bin") as file:
            while file.read(1)[0] != 0:
                pos = tuple(file.read(2)[0])
                chunk = []
                while True:
                    ident = file.read(1)[0]
                    
