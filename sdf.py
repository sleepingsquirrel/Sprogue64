from random import randint
import numpy as np
from math import floor,cos,sin,dist
class signed_distance_function:
    def __init__(self, parent):
        self.parent = parent
        self.w = self.parent.world

    def circle(self, x1,y1,x2,y2,r):
        dist(x1,y1,x2,y2) - r

    def sdf(self):
        out = np.zeros((500,4), dtype="uint8")

        for i in range(500):
            rrot = rot - self.fov / 2 + self.fov * (i/500)
            rx = pos[0]
            ry = pos[1]
            distance = 0
            d = 0
            for depth in range(100):
                d = min(abs(ry),abs(rx)) 
                d = min(d, abs(circle(ry,rx,4,4,1)))

                if -0.001 < d and d < 0.001:
                    yhes = min(round((40 / distance / cos(rrot - rot))), height) 
                    break
                if d > 10:
                    break
                rx += sin(rrot) * d
                ry += cos(rrot) * d
                distance += d



    def __call__(self):
        self.sdf()
        return np.array([randint(0, 255) for i in range(500 * 4)], dtype="uint8")