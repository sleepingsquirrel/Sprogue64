import pygame
import random
from time import sleep
import moderngl as mgl
from PIL import Image
import numpy as np
from pygame.locals import *
from math import floor
from shaders import shader_storage
from sdf import signed_distance_function
import math
import platform

class renderer:
    def __init__(self, parent):
        pygame.init()
        self.parent = parent
        window = pygame.display.set_mode(self.parent.display, OPENGL|DOUBLEBUF|RESIZABLE, vsync=True)
        self.ctx = mgl.create_context()
        self.sdf = signed_distance_function(self)
        self.shaders = shader_storage()
        self.make_shaders()
        
    
    def render(self):
        self.get_walls()
        self.vao.render()

    def get_walls(self):
        walls = self.sdf()
        self.tex = self.ctx.texture((500,1), 4,walls.tobytes())
        # self.tex.filter = mgl.NEAREST, mgl.NEAREST
        self.tex.repeat_x = False
        # print(self.tex.samples)
        # self.tex.anisotropy = 16.0
        self.tex.use(0)
        self.shader["atlas"] = 0

    
    def make_shaders(self):
        vertex = self.shaders.vert_wall
        fragment = self.shaders.frag_wall
        self.shader = self.ctx.program(vertex_shader = vertex, fragment_shader = fragment)
        vbo = self.ctx.buffer(np.array((-1,-1,1,1,1,-1,1,1,-1,1,-1,-1), dtype = np.float32).tobytes())
        self.vao = self.ctx.vertex_array(self.shader, vbo, "apos")
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
        