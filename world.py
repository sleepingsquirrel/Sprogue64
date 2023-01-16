import numpy as np
import csv
import pickle

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
    chunk_size = 16
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
    
    def csv_to_bin(self):
        data = self.load_csv()
        

    #for internal use only, use csv_to_bin instead
    def load_level(self,name = "level.spr"):
        retrieved_data = pickle.load(name)


if __name__ == "__main__":
    test = world()
    test.load_csv()
