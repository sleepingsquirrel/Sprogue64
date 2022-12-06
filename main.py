import pygame
from pygame.locals import *

class window:
    def __init__(self):
        pygame.display.set_mode((500,500), OPENGL|DOUBLEBUF|RESIZABLE)
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
