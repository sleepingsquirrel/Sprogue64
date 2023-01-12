from random import randint
import numpy as np
from math import floor,cos,sin,sqrt,hypot

#gives data of the height of walls as texture
class signed_distance_function:
    def __init__(self, parent):
        self.parent = parent
        self.w = self.parent.world
        self.p = self.parent.player
        self.fov = self.parent.fov

    def circle(self,ax, ay, bx, by, r):
        return hypot(ax,ay,bx,by) - r
    
    def semi_circle(self,rx,ry,cx,cy,r,l):
        max(rx*cos(r)+ry*sin(r),self.circle(rx,ry,cx,cy,l))

    def line(self,pos,ishorizontal,c,l):
        cpos = [0,0]
        cpos[int(ishorizontal)] = pos[int(ishorizontal)]
        cpos[int(not ishorizontal)] = c
        max(abs(pos[int(ishorizontal)]),self.circle(pos[0],[pos[1]],cpos[0],cpos[1],l/2))



    def getchunks(self,rx,ry):
        world = self.w.map
        # try:
        return [world[floor(rx//16 + i % 3 - 1)][floor(ry//16 + i // 3 - 1)] for i in range(9)]
        # except:
        #     print(rx,ry)

    def objdis(self,obj,rx,ry):
        if obj.type == 1:
            return self.circle(obj.x,obj.y,obj.w)
        elif obj.type == 2:
            return self.line(rx if obj.ishorizontal else ry,obj.ishorizontal,obj.c,obj.l)
        elif obj.type == 3:
            return self.semi_circle(rx,ry,obj.x,obj.y,obj.r,obj.w)
             

    def rdis(self,rx,ry): 
        chunk = self.getchunks(rx,ry)
        d = min(rx,ry)
        d = min(min([min([self.objdis(obj,rx,ry) for obj in chunk[i]] + [10000]) for i in range(9)]),d)
        return d

    


    def sdf(self):
        out = np.zeros((500,4), dtype="uint8")

        for i in range(500):
            rrot = self.p.rot - self.fov / 2 + self.fov * (i/500)
            rx = self.p.x
            ry = self.p.y
            distance = 0
            d = 0

            for depth in range(200):
                d = self.rdis(rx,ry)
                # d = min(d, abs(self.circle(ry,rx,4,4,1)))

                if abs(d) < 0.001:
                    out[i][0] = min(round((40 / distance / cos(rrot - self.p.rot + 0.00001231412341234321))), 255) 
                    out[i][1] = depth
                    # out[i][2]
                    # out[i][3]
                    break
                if d > 10:
                    break
                rx += sin(rrot) * d
                ry += cos(rrot) * d
                distance += d
                # print(distance)
        out.dtype = "float32"
        return out



    def __call__(self):
        return np.array(self.sdf())