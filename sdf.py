from random import randint
import numpy as np
from math import floor,cos,sin,sqrt
import numpy as np

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
        return max(abs(pos[ishorizontal]-(x if ishorizontal else y)),self.circle(pos[0],pos[1],x,y,l/2))

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

    def sdf(self):
        out = np.zeros((500,4), dtype="uint8")

        for i in range(200):
            rrot = self.p.rot - self.fov / 2 + self.fov * (i/200)
            rx = self.p.x
            ry = self.p.y
            distance = 0
            d = 0

            for depth in range(100):
                d = self.rdis(rx,ry)
                # d = min(d, abs(self.circle(ry,rx,4,4,1)))

                if abs(d) < 0.1:
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