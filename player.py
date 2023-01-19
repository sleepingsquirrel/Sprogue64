from math import tan

class player:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.gold = 0 
        self.rot = -3.1415
        self.keys = [False, False, False, False, False, False]
        self.hp = 100

    def shoot(self, entities):
        for i in entities:
            if ((self.x - i.x) / (self.y - i.y)) % tan(self.rot) < i.w:
                i.hp -= 100

