import pygame
from sprite import Sprite

class SpriteInteractive(Sprite):

    def __init__(self, x, y, filename, centered):
        Sprite.__init__(self, x, y, filename, centered)

    def draw(self, screen):
        screen.blit(self.surface, (self.x + self.ox, self.y + self.oy))

    
    

