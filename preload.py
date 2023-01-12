import csv
from world import wall
from math import hypot
def load_csv(self):
    shapes = []
    with open('map.csv') as file:
        reader = csv.DictReader(file)
        for i in reader:
            current = wall(i.id, i.r, i.x, i.y, i.w, i.h)
            shapes.append(current)
        return shapes
def semicircle_convert(x1,y1,x2,y2,r):
    #get middle
    cx,cy = (x1+x2)/2,(y1+y2)/2
    rad = abs(hypot(cx,cy,x1,y1))
    return wall(3,r,cx,cy,rad,0)

def line_convert(x1,y1,x2,y2):
    
    w = wall()




# opening the CSV file
with open('world.csv', mode ='r') as file:

    # reading the CSV file
    reader = csv.DictReader(file)

    # displaying the contents of the CSV file
    for obj in reader:
