import pygame
import math

from track import Track
from tile import TileId

class Car():
    def __init__(self, x, y, path):
        self.image = pygame.image.load(path).convert_alpha()
        self.x = x
        self.y = y
        self.origin_x = -self.image.get_width() / 2
        self.origin_y = -self.image.get_height() / 2
        self.angle = 0
        self.velocity = 0
        self.max_speed = 400
        self.out_of_control_timer = 0

    def next_x(self, dt):
        return self.x + self.velocity * math.cos(math.radians(self.angle)) * dt

    def next_y(self, dt):
        return self.y + self.velocity * math.sin(math.radians(self.angle)) * dt

    def check_collision(self, dt):
        next_tile_row = math.floor(self.next_y(dt) / Track.TILE_HEIGHT)
        next_tile_col = math.floor(self.next_x(dt) / Track.TILE_WIDTH) + 1
        # Track col and row must be in config limit
        if next_tile_col < 0 or next_tile_row < 0 or next_tile_row >= Track.TRACK_ROWS or next_tile_col >= Track.TRACK_COLS:
            return
        # Collision
        collided_tile = Track.GRID[next_tile_row * Track.TRACK_COLS + next_tile_col]
        if TileId(collided_tile) is TileId.block and not self.out_of_control_timer > 0:
            self.bounce()

    def bounce(self):
        self.out_of_control_timer = 30
        self.velocity = -self.velocity / 4
    
    def update(self, dt):
        if self.out_of_control_timer > 0:
            self.out_of_control_timer = self.out_of_control_timer - 1
        else:
            self.check_collision(dt)
        self.x = self.next_x(dt)
        self.y = self.next_y(dt)
        self.velocity = self.velocity * 0.96

    def turn_left(self, dt):
        if not self.out_of_control_timer > 0:
            self.angle = self.angle - 180 * dt

    def turn_right(self, dt):
        if not self.out_of_control_timer > 0:
            self.angle = self.angle + 180 * dt

    def accelerate(self):
        if not self.out_of_control_timer > 0:
            self.velocity = self.velocity + 35
            if self.velocity > self.max_speed:
                self.velocity = self.max_speed

    def draw(self, screen):
        r_car = pygame.transform.rotate(self.image, -self.angle)
        screen.blit(r_car, (self.x, self.y))
