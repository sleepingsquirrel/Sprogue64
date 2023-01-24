from math import tan,sin,cos

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

    def dis(self,lines,rot):
        di = 100
        rline = [self.x,self.y,self.x + sin(rot) * di,self.y + cos(rot) * di]
        return min([self.parent.sdf.distance(self.parent.sdf.line_intersection(*rline,*line)) for line in lines])
    
    def move(self,rot,speed):
        self.x += sin(rot) * speed
        self.y += cos(rot) * speed

