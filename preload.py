import csv
from world import wall
from math import sqrt,radians
import pickle
from PIL import Image

def preload(map = "map.csv",level_name = "level.spr"):
    with open(level_name, "wb") as file:
        stuff = load_csv('map.csv')
        print(stuff)
        pickle.dump(stuff, file)

def load_csv(map):
    shapes = []
    with open(map) as file:
        reader = csv.DictReader(file)
        for i in reader:
            print(i["id"])
            print(make_shape(i))
            shapes.append(make_shape(i))

        return shapes

def make_shape(obj):
    match int(obj["id"]):
        case -1:
            return semicircle_convert(float(obj["x"])/8,float(obj["y"])/8,float(obj["w"])/8,radians(float(obj["r"])))
        case 0:
            return circle_convert(float(obj["x"])/8,float(obj["y"])/8,float(obj["w"])/8)
        case 1:
            return line_convert(float(obj["x"])/8,float(obj["y"])/8,float(obj["w"])/8,float(obj["h"])/8) 
def length(ax,ay,bx,by):
        return sqrt((ax-bx)**2 + (ay-by)**2)

def semicircle_convert(x,y,w,r):
    #get middle
    
    # cx,cy = (x1+x2)/2,(y1+y2)/2
    # rad = abs(length(cx,cy,x1,y1))
    # print(cx,cy,rad,r)
    return wall(3,r,x,y,w,0)

def line_convert(x1,y1,x2,y2):
    is_horizontal = int(abs(x1-x2) < abs(y1-y2))
    p1 = [x1,y1]
    p2 = [x2,y2]
    mid = [(p1[is_horizontal]+p2[is_horizontal])/2,p1[int(not is_horizontal)]]
    r = abs(p1[is_horizontal]-p2[is_horizontal]) /2
    cx,cy = (x1+x2)/2,(y1+y2)/2
    return wall(2,is_horizontal,cx,cy,r,None)

def circle_convert(x,y,r):
    return wall(1,0,x,y,r,0)
    
preload()