import pygame
from pygame.locals import *
from gl import renderer
from world import wall
from player import player
from world import world

#main loop, the main class that all others are connected to
class window:
    display = (500,500)
    fov = 60
    def __init__(self):
        self.player = player()
        #grab world gl and player classes
        self.world = world()
        self.gl = renderer(self)
    
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
            #render screen
            self.gl.render()
            #update screen
            pygame.display.flip()

if __name__ == "__main__":
    window()
