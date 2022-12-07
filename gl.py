import pygame
import random
from time import sleep
import moderngl as mgl
from PIL import Image
import numpy as np
from pygame.locals import *
from math import floor, shaders_storage
import math
from shaders import shader

class renderer:
    def __init__(self, parent):
        pygame.init()
        self.parent = parent
        window = pygame.display.set_mode(self.parent.display, OPENGL|DOUBLEBUF|RESIZABLE)
        self.ctx = mgl.create_context()
    
    def make_shaders(self):
        vertex = self.shaders.vert_vert
        fragment = self.shaders.frag_
        self.shader = self.ctx.program(vertex_shader = vertex, fragment_shader = fragment)
        # self.len_atlas_loc = self.shader['len_atlas']
        # self.atlas_loc = self.shader['atlas']
        # self.scale_uniform = self.shader["scale"]
        # self.pos_uniform = self.shader["pos"]
        # self.atlas_loc = 0
        # self.shader["avgatlas"] = 2
        # self.atlas.use(0)
        # self.player_tex.use(1)
        # self.avgatlas.use(2)

        # self.player_shader = self.ctx.program(vertex_shader = self.shaders.vert_player, geometry_shader = self.shaders.geo_player, fragment_shader = self.shaders.frag_player)
        # self.player_shader['len_atlas'].value = self.player_dimensions
        # self.player_shader['atlas'].value = 1



        print('shaders: complete')
        