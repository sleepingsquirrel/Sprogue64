from math import tan

class player:
    def __init__(self):
        self.x = 0
        self.y = 5
        self.gold = 0 
        self.rot = 0
        self.keys = [False, False, False, False, False, False]
        self.hp = 100

    def shoot(self, entities):
        for i in entities:
            if ((self.x - i.x) / (self.y - i.y)) % tan(self.rot) < i.w:
                i.hp -= 100

