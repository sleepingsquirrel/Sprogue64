from math import tan,sin,cos
import math

class player:
    def __init__(self,parent):
        self.parent = parent
        self.x = 59/4+0.1
        self.y = 98/4+0.2
        self.gold = 0 
        self.rot = 0
        self.keys = [False, False, False, False, False, False]
        self.hp = 100

    def shoot(self, entities):
        for i in entities:
            if ((self.x - i.x) / (self.y - i.y)) % tan(self.rot) < i.w:
                i.hp -= 100

    def min_dis(self,lines):
        return min([self.dis(lines,self.rot + (math.pi/4)*i) for i in range(8)])



    def dis(self,lines,rot):
        di = 100
        rline = [self.x,self.y,self.x + sin(rot) * di,self.y + cos(rot) * di]
        minu = 1000.0
        for i in lines:
            b = self.parent.gl.sdf.line_intersection(*rline,*[i.x,i.y,i.w,i.h])
            if b[0]:
                distance = self.parent.gl.sdf.length(self.x,self.y,b[1],b[2])

                if distance < minu:
                    minu = distance
        if minu < 0.3:
            self.x -= sin(rot) *( 0.3 - minu)
            self.y -= cos(rot) *( 0.3 - minu)
        return minu

    def move(self,rot,speed):
        self.x += sin(rot) * speed
        self.y += cos(rot) * speed

