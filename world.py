import numpy as np

class wall:
    def __init__(self,wtype,rot,x,y,w,h):
        self.type = wtype
        self.rot = rot
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
# first byte is either 0 (end) or anything else (continues)
# next two, chunk x, chunk y
# next byte is object id
# next five bytes, rot, xpos, ypos, width, height
# repeat from object id until id is 0

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
                    if ident == 0:
                        break
                    chunk.append(wall(ident, *file.read(5)))
                self.map[(pos)]
                    
