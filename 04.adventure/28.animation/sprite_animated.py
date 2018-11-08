import pygame
from sprite_controlled import SpriteControlled
from animation import Animation

class SpriteAnimated(SpriteControlled):
    def __init__(self, x, y, centered, speed, base_animation):
        self.animations = {}
        self.animations["idle"] = Animation(1, 50, "sprite_idle.png")
        self.animations["walking"] = Animation(8, 10, "sprite_walking.png")
        SpriteControlled.__init__(self, x, y, "sprite_idle.png", centered, speed)
        self.current_animation = base_animation

    def update(self):
        self.animations[self.current_animation].update()
        SpriteControlled.update(self)
        if self.is_moving:
            self.current_animation = "walking"
        else:
            self.current_animation = "idle"

    def draw(self, screen):
        screen.blit(self.animations[self.current_animation].get_surface(), (self.x + self.ox, self.y + self.oy))
