import pygame
import os
from enum import Enum

class RoadId(Enum):
    road = 0
    block = 1
    flag = 3
    turn = 4
    grass = 5


class Tile():
    def __init__(self, x, y, tile_id):
        self.x = x
        self.y = y
        self.id = tile_id
        path = os.path.abspath('.') + '/'
        if tile_id == RoadId.road:
            self.image = pygame.image.load(path+"images/road.png").convert_alpha()
        if tile_id == RoadId.grass:
            self.image = pygame.image.load(path+"images/grass.png").convert_alpha()
        if tile_id == RoadId.block:
            self.image = pygame.image.load(path+"images/block.png").convert_alpha()
        if tile_id == RoadId.turn:
            self.image = pygame.image.load(path+"images/turn.png").convert_alpha()
        else:
            self.image = pygame.image.load(path+"images/flag.png").convert_alpha()
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

