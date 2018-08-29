import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite

class Scene:
    
    def __init__(self, name, background_file, ground_file):
        self.name = name