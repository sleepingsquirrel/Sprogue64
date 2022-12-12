from random import randint
import numpy as np
from math import floor,cos,sin,dist

class signed_distance_function:
    def __init__(self, parent):
        self.parent = parent
        self.w = self.parent.world
        self.p = self.parent.player

    def circle(self, x1,y1,x2,y2,r):
        dist(x1,y1,x2,y2) - r

    def sdf(self):
        out = np.zeros((500,4), dtype="uint8")

        for i in range(500):
            rrot = self.p.rot - self.fov / 2 + self.fov * (i/500)
            rx = self.p.x
            ry = self.p.x
            distance = 0
            d = 0

            for depth in range(255):
                d = min(abs(ry),abs(rx)) 
                d = min(d, abs(self.circle(ry,rx,4,4,1)))

                if -0.001 < d and d < 0.001:
                    out[i][0] = min(round((40 / distance / cos(rrot - self.p.rot))), 255) 
                    out[i][1] = depth
                    # out[i][2]
                    # out[i][3]
                    break
                if d > 10:
                    break
                rx += sin(rrot) * d
                ry += cos(rrot) * d
                distance += d
        out.dtype = "float32"
        return out



    def __call__(self):
        return np.array(self.sdf())