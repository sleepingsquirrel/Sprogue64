import numpy as np
import csv
import pickle
from math import floor

class wall:
    def __init__(self,x,y,w,h,color):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        

        
# first byte is either 0 (end) or anything else (continues)
# next two, chunk x, chunk y
# next byte is object id
# next five bytes, rot, xpos, ypos, width, height
# repeat from object id until id is 0

class world:
    chunk_size = 16
    def __init__(self):
        self.map = [[[] for i in range(255)] for _ in range(255)]
        self.scale = 16
        self.load_level()

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
                self.map[pos[0],pos[1]].append(chunk)
    
    # def csv_to_bin(self):
    #     data = self.load_csv()
        

    #for internal use only, use csv_to_bin instead
    def load_level(self,name = "level.spr"):
        with open(name, "rb") as level:
            retrieved_data = pickle.load(level)
            # print(retrieved_data)
            for i in retrieved_data:
                assert type(i) == wall
                x = floor(i.x / self.scale)
                y = floor(i.y / self.scale)
                self.map[x][y].append(i)
                print(i.x,i.y)


# if __name__ == "__main__":
#     test = world()
#     test.load_csv()
