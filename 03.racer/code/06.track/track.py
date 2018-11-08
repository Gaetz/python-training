import pygame

from tile import Tile, TileId

class Track():

    TRACK_COLS = 20
    TRACK_ROWS = 15
    TRACK_WIDTH = 40
    TRACK_HEIGHT = 40
    GRID = [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5,
            5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
            1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 1, 1, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 0, 0, 1,
            1, 0, 0, 1, 1, 0, 0, 1, 5, 5, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1,
            1, 0, 0, 1, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1,
            1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1,
            1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 1, 0, 0, 1,
            1, 0, 0, 1, 0, 0, 4, 0, 0, 0, 4, 0, 0, 1, 0, 0, 1, 0, 0, 1,
            1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 1,
            1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
            1, 3, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,
            1, 3, 0, 0, 0, 0, 1, 5, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5]

    def __init__(self):
        self.tiles = []
        tile_y = 0
        tile_x = 0
        tile_index = 0
        for i in range(0, Track.TRACK_ROWS):
            for j in range(0, Track.TRACK_COLS):
                tile_type = TileId(Track.GRID[tile_index])
                new_tile = Tile(tile_x, tile_y, tile_type)
                self.tiles.append(new_tile)
                # For next iteration
                tile_x = (tile_x + Track.TRACK_WIDTH) % (Track.TRACK_COLS * Track.TRACK_WIDTH)
                tile_index = tile_index + 1
            tile_y = (tile_y + Track.TRACK_HEIGHT) % (Track.TRACK_ROWS * Track.TRACK_HEIGHT)

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)
        