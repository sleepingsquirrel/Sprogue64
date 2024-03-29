import pygame
from pygame.locals import *
from gl import renderer
from world import wall
from player import player
from world import world
import math
from math import sin,cos
from entities import entity

#main loop, the main class that all others are connected to
class window:
    keys = {K_w:False,K_a: False,K_s:False,K_d:False,K_SPACE:False}
    display = (500,500)
    fov = math.pi / 2
    titleon = True
    def __init__(self):
        self.player = player(self)
        #grab world gl and player classes
        self.world = world()
        self.gl = renderer(self)
        self.clock = pygame.time.Clock()
    
        #run main loop
        self.run()
    
    def run(self):

        #frame count

        entity_render_dist = 2
        #GET RID OF THIS LATER
        # entities = [entity("Sprite-0001.png", 1, 1, 1, 1)]
        #GET RID OF THAT LATER

        self.f = 0
        self.running = True
        while self.running:
            if self.titleon:
                for i in self.keys.keys():
                    if (self.keys[i]):
                        self.titleon = False
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
                # if self.player.min_dis(self.gl.sdf.lines) > 0.3:
                self.player.x += sin(self.player.rot) * speed
                self.player.y += cos(self.player.rot) * speed
                self.player.min_dis(self.gl.sdf.lines)

            if(self.keys[K_a]):
                self.player.rot -= 0.1001
            if(self.keys[K_s]):
                # if self.player.min_dis(self.gl.sdf.lines) > 0.3:
                
                self.player.x -= sin(self.player.rot) * speed
                self.player.y -= cos(self.player.rot) * speed
                self.player.min_dis(self.gl.sdf.lines)
            if(self.keys[K_d]):
                self.player.rot += 0.1001
            # if (self.keys[K_SPACE]):
            #     self.player.shoot(entities)
            
            # for i in entities:
            #     if math.dist([i.x, i.y], [self.player.x, self.player.y]) < entity_render_dist:
            #         i.show()
            #         if i.update(self.player):
            #             #self.running = False
            #             pass
                
                
            #render screen
            self.gl.render()
            # self.gl.sdf.sdf()
            #update screen
            pygame.display.flip()
            self.clock.tick(60)
            if not self.f % 60:
                print(self.clock.get_fps(),self.player.x,self.player.y)


if __name__ == "__main__":
    window()
