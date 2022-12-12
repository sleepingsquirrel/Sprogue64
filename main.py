import pygame
from pygame.locals import *
from gl import renderer
from world import wall
from player import player
from world import world

class window:
    display = (500,500)
    fov = 60
    def __init__(self):
        self.world = world()
        self.gl = renderer(self)
        self.player = player()
        self.run()
    
    def run(self):
        self.f = 0
        self.running = True
        while self.running:
            self.f += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            self.gl.render()
            pygame.display.flip()

if __name__ == "__main__":
    window()
