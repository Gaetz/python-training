import pygame
from sprite import Sprite

class Warp(Sprite):
    def __init__(self, x, y, filename, centered, to_scene):
        Sprite.__init__(self, x, y, filename, centered)
        self.to_scene = to_scene[0]
        self.to_scene_x = to_scene[1]