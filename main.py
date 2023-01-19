import pygame
from pygame.locals import *
from gl import renderer
from world import wall
from player import player
from world import world
import math
from math import sin,cos
#main loop, the main class that all others are connected to
class window:
    keys = {K_w:False,K_a: False,K_s:False,K_d:False}
    display = (500,500)
    fov = math.pi / 2
    def __init__(self):
        self.player = player()
        #grab world gl and player classes
        self.world = world()
        self.gl = renderer(self)
        self.clock = pygame.time.Clock()
    
        #run main loop
        self.run()
    
    def run(self):
        #frame count
        self.f = 0
        self.running = True
        while self.running:
            self.f += 1
            #make the x button quit out of the window
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key in self.keys:
                        self.keys[event.key] = True
                if event.type == KEYUP:
                    if event.key in self.keys:
                        self.keys[event.key] = False
            speed = 0.0501
            if(self.keys[K_w]):
                self.player.x += sin(self.player.rot) * speed
                self.player.y += cos(self.player.rot) * speed
            if(self.keys[K_a]):
                self.player.rot -= 0.1001
            if(self.keys[K_s]):
                self.player.x -= sin(self.player.rot) * speed
                self.player.y -= cos(self.player.rot) * speed
            if(self.keys[K_d]):
                self.player.rot += 0.1001
                
                
            #render screen
            self.gl.render()
            #update screen
            pygame.display.flip()
            self.clock.tick(60)
            if not self.f % 60:
                print(self.clock.get_fps(),self.player.x,self.player.y)


if __name__ == "__main__":
    window()
