from random import randint
import numpy as np
from math import floor,cos,sin,sqrt

#gives data of the height of walls as texture
class signed_distance_function:
    def __init__(self, parent):
        self.parent = parent
        self.w = self.parent.world
        self.p = self.parent.player
        self.fov = self.parent.fov

    def length(self,ax,ay,bx,by):
        return sqrt((ax - bx) ** 2 + (ay - by) ** 2)

    def circle(self,ax, ay, bx, by, r):
        return self.length(ax,ay,bx,by) - r

    def sdf(self):
        out = np.zeros((500,4), dtype="uint8")

        for i in range(500):
            rrot = self.p.rot - self.fov / 2 + self.fov * (i/500)
            rx = self.p.x
            ry = self.p.y
            distance = 0
            d = 0

            for depth in range(255):
                d = min(abs(ry),abs(rx)) 
                # d = min(d, abs(self.circle(ry,rx,4,4,1)))

                if -0.001 < d and d < 0.001:
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