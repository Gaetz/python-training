import pygame
import os
from enum import Enum

class TileId(Enum):
    road = 0
    block = 1
    flag = 3
    turn = 4
    grass = 5

class Tile():
    def __init__(self, x, y, tile_id):
        self.x = x
        self.y = y
        path = os.path.abspath('.') + '/'
        if tile_id is TileId.road:
            self.image = pygame.image.load(path+"images/road.png").convert_alpha()
        elif tile_id is TileId.grass:
            self.image = pygame.image.load(path+"images/grass.png").convert_alpha()
        elif tile_id is TileId.block:
            self.image = pygame.image.load(path+"images/block.png").convert_alpha()
        elif tile_id is TileId.turn:
            self.image = pygame.image.load(path+"images/turn.png").convert_alpha()
        else:
            self.image = pygame.image.load(path+"images/flag.png").convert_alpha()
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

