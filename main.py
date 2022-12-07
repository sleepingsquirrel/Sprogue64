import pygame
from pygame.locals import *
from gl import renderer

class window:
    def __init__(self):
        self.gl = renderer()
        self.run()
    
    def run(self):
        self.f = 0
        self.running = True
        while self.running:
            self.f += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

if __name__ == "__main__":
    pygame.init()
    window()
