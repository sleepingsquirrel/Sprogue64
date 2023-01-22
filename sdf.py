from random import randint
import numpy as np
from math import floor,cos,sin,sqrt,degrees,atan
import math
import numpy as np
import pygame

#gives data of the height of walls as texture
class signed_distance_function:
    def __init__(self, parent):
        self.parent = parent
        self.w = self.parent.world
        self.p = self.parent.player
        self.fov = self.parent.fov
        self.map = [[["no"] for i in range(255)] for _ in range(255)]

    def length(self,ax,ay,bx,by):
        return sqrt((ax-bx)**2 + (ay-by)**2)

    def circle(self,ax, ay, bx, by, r):
        return self.length(ax,ay,bx,by) - r
    
    def semi_circle(self,rx,ry,cx,cy,r,l):
        return max((rx - cx)*cos(r)+(ry - cy)*sin(r),self.circle(rx,ry,cx,cy,l))

    def line(self,pos,ishorizontal,x,y,l):
        return max(abs(pos[ishorizontal]- (x if ishorizontal else y)),self.circle(pos[0],pos[1],x,y,l/2))

    def objdis(self,obj,rx,ry):
        if obj.type == 1:
            return self.circle(rx,ry,obj.x,obj.y,obj.w)
        elif obj.type == 2:
            return self.line(rx,ry,bool(obj.rot),obj.x,obj.y,obj.w)
        if obj.type == 3:
            return self.semi_circle(rx,ry,obj.x,obj.y,obj.rot,obj.w)
        else:
            return 10000
                         

    def rdis(self,rx,ry): 
        world = self.w.map
        scale = self.w.scale
        # print(chunk)
        # d = min(rx,ry,scale,abs(rx-15),abs(ry-15))
        # d = self.semi_circle(rx,ry,0,0,2,1)
        # d = min(d, self.semi_circle(rx,ry,5,5,1,1))
        # d = min(d,max((rx-5)+(ry-5),self.circle(rx,ry,5,5,2)))
        d = scale
        # d = min(rx,ry,self.w.scale,abs(rx-15),abs(ry-15))
        if rx > 0 and ry >= 0:
            if self.map[int(rx//scale)][int(ry//scale)] != ["no"]:
                chunk = self.map[int(rx//scale)][int(ry//scale)]
            else:
                chunk = []
                for x in range(3):
                    for y in range(3):
                        for i in world[int(rx//scale+x-1)][int(ry//scale + y)]:
                            print("guh huh")
                            chunk.append(i)
                self.map[int(rx//scale)][int(ry//scale)] = chunk
            if chunk:
                d = min(d,min([self.objdis(i,rx,ry) for i in chunk]))
        # d = self.circle(rx,ry,2,0,1)


            

        # print([5] + [100])
        # beans = [min([self.objdis(obj,rx,ry) for obj in chunk[i]] + [10000]) for i in range(9)]
        # if chunk != []:
        #     print(chunk)


        #to do make function that crawls array to find objs


        return d

    
    def min_array(self,lis):
        mind = 10000
        for arr in lis:
            if arr:
                if type(arr) == type([]):
                    mind = min(mind,self.min_array(arr))
                else:
                    return min([self.objdis(i) for i in lis])
        return mind

    def line_intersection(self,x1, y1, x2, y2, x3, y3, x4, y4):
        # Calculate the coefficients of the two lines
        a1 = y2 - y1
        b1 = x1 - x2
        c1 = a1 * x1 + b1 * y1

        a2 = y4 - y3
        b2 = x3 - x4
        c2 = a2 * x3 + b2 * y3

        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return [None]  # The lines are parallel

        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant

        # Check if the intersection point is on both line segments
        if (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2) and
            min(x3, x4) <= x <= max(x3, x4) and
            min(y3, y4) <= y <= max(y3, y4)):
            return [True,x, y]
        else:
            return [None]



    def sdf(self):
        p = self.p
        out = np.zeros((500,4), dtype="uint8")
        rx = self.p.x
        ry = self.p.y

        start = None
        last = None
        for i in range(500):
            rrot = self.p.rot - self.fov / 2 + self.fov * (i/500)
            dis = 1000
            rline = [rx,ry,rx + sin(rrot) * dis,ry + cos(rrot) * dis]
            li = self.line_intersection(*rline,*[10,10,11,10])
            if li[0]:
                if start == None:
                    distance = self.length(rx,ry,li[1],li[2]) 
                    start = [rrot, min(round((40 / distance / cos(rrot - self.p.rot + 0.00001231412341234321))), 255)]
                last = [rrot,li]
        if last == None:
            return out
        li = last[1]
        distance = self.length(rx,ry,li[1],li[2])
        last[1] = min(round((40 / distance / cos(rrot - self.p.rot + 0.00001231412341234321))), 255)
        
                
        for i in range(500):
            rrot = self.p.rot - self.fov / 2 + self.fov * (i/500)
            if rrot >= start[0] and rrot <= last[0]:
                # if rrot - start[0] == 0:
                #     out[i][0] = start[0]
                #     continue
                if start[1] == last[1]:
                    out[i][0] = start[1]
                    continue
                print(start,last)
                slope = (start[1] - last[1])/(last[0] - start[0])
                print(slope)
                out[i][0] = min(int(slope * rrot + start[0]),255)
                # out[i][0] = ((last[0] - start[0]) / (rrot - start[0])) * (start[1] - last[1]) + start[1]

                

        # for i in range(500):
        #     rrot = self.p.rot - self.fov / 2 + self.fov * (i/500)
        #     rx = self.p.x
        #     ry = self.p.y
        #     distance = 0
        #     d = 0

        #     for depth in range(200):
        #         d = self.rdis(rx,ry)
        #         # d = min(d, abs(self.circle(ry,rx,4,4,1)))

        #         if abs(d) < 0.001:
        #             out[i][0] = min(round((40 / distance / cos(rrot - self.p.rot + 0.00001231412341234321))), 255) 
        #             out[i][1] = depth
        #             # out[i][2]
        #             # out[i][3]
        #             break
        #         if d > 10:
        #             break
        #         rx += sin(rrot) * d
        #         ry += cos(rrot) * d
        #         distance += d
        #         # print(distance)
        out.dtype = "float32"
        return out



    def __call__(self):
        return np.array(self.sdf())