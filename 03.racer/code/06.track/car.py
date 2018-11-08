import pygame
import math

class Car():
    def __init__(self, x, y, path):
        self.image = pygame.image.load(path).convert_alpha()
        self.x = x
        self.y = y
        self.origin_x = -self.image.get_width() / 2
        self.origin_y = -self.image.get_height() / 2
        self.angle = 0
        self.velocity = 0
        self.max_speed = 800
    
    def update(self, dt):
        self.x = self.x + self.velocity * math.cos(math.radians(self.angle)) * dt
        self.y = self.y + self.velocity * math.sin(math.radians(self.angle)) * dt
        self.velocity = self.velocity * 0.96        

    def turn_left(self, dt):
        self.angle = self.angle - 180 * dt

    def turn_right(self, dt):
        self.angle = self.angle + 180 * dt

    def accelerate(self):
        self.velocity = self.velocity + 35
        if self.velocity > self.max_speed:
            self.velocity = self.max_speed

    def draw(self, screen):
        r_car = pygame.transform.rotate(self.image, -self.angle)
        screen.blit(r_car, (self.x - self.origin_x, self.y - self.origin_y))
