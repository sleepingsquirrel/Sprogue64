import csv
from world import wall
from math import hypot
import pickle

def preload(map = "map.csv",level_name = "level.spr"):
    with open(level_name, "ab") as file:
        pickle.dump(load_csv('map.csv'), file)

def load_csv(map):
    shapes = []
    with open(map) as file:
        reader = csv.DictReader(file)
        for i in reader:
            shapes.append(make_shape(i))
        return shapes

def make_shape(obj):
    match obj["id"]:
        case 1:
            return circle_convert(obj["x"],obj["y"],obj["w"])
        case 2:
            return line_convert(obj["x"],obj["y"],obj["w"],obj["h"])
        case 3:
            return semicircle_convert(obj["x"],obj["y"],obj["w"],obj["h"],obj["rot"])

def semicircle_convert(x1,y1,x2,y2,r):
    #get middle
    cx,cy = (x1+x2)/2,(y1+y2)/2
    rad = abs(hypot(cx,cy,x1,y1))
    return wall(3,r,cx,cy,rad,0)

def line_convert(x1,y1,x2,y2):
    is_horizontal = int((x1-x2) < (y1-y2))
    p1 = [x1,y1]
    p2 = [x2,y2]
    mid = [(p1[is_horizontal]+p2[is_horizontal])/2,p1[int(not is_horizontal)]]
    r = abs(p1[is_horizontal]-p2[is_horizontal]) /2
    w = wall(2,is_horizontal,mid[0],mid[1],r,None)

def circle_convert(x,y,r):
    return wall(1,0,x,y,r,0)
preload()