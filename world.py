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
        self.map = [[[] for i in range(255)] for _ in range(255)]
        self.load_from_file()

    def load_from_file(self):
        with open("world/world.bin") as file:
            if not len(file.read()):
                return
            while file.read(1)[0] != 0:
                pos = tuple(file.read(2)[0])
                chunk = []
                while True:
                    ident = file.read(1)[0]
                    if ident == 0:
                        break
                    chunk.append(wall(ident, *file.read(5)))
                self.map[pos[0],pos[1]] = chunk
                    
