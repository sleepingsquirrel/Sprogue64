import pygame
from pygame.locals import *
from gl import renderer

class window:
    display = (512,500)
    def __init__(self):
        self.gl = renderer(self)
        self.run()

    def make_world(self):
        pass
    
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
