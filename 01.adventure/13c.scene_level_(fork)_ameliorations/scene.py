import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp

class Scene:
    
    def __init__(self, background_file, ground_file):
        self.background = Sprite(0, 0, background_file, False)
        self.ground = Sprite(0, 0, ground_file, False)

    def load(self):
        pass

    def inputs(self, events):
        pass

    def update(self, change_scene):
        pass

    def draw(self, screen):
        pass
    

