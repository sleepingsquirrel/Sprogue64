import numpy as np
import csv
import pickle
from math import floor

class wall:
    def __init__(self,x,y,w,h,color):
        scale = 8
        self.x = float(x)/scale
        self.y = float(y)/scale
        self.w = float(w)/scale
        self.h = float(h)/scale
        self.color = color
        

        
# first byte is either 0 (end) or anything else (continues)
# next two, chunk x, chunk y
# next byte is object id
# next five bytes, rot, xpos, ypos, width, height
# repeat from object id until id is 0

class world:
    chunk_size = 16
    def __init__(self):
        self.lines = []
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
        
    def hex_to_rgb(self,value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    #for internal use only, use csv_to_bin instead
    def load_level(self,name = "map.csv"):
         with open(name) as file:
            reader = csv.DictReader(file)
            for i in reader:
                self.lines.append(wall(i["x1"],i["y1"],i["x2"],i["y2"],self.hex_to_rgb(i["colour"])))
        # with open(name, "rb") as level:
        #     retrieved_data = pickle.load(level)
        #     # print(retrieved_data)
        #     for i in retrieved_data:
        #         assert type(i) == wall
        #         x = floor(i.x / self.scale)
        #         y = floor(i.y / self.scale)
        #         self.map[x][y].append(i)
        #         print(i.x,i.y)


# if __name__ == "__main__":
#     test = world()
#     test.load_csv()
