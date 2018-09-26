import math
from sprite import Sprite

class SpriteControlled(Sprite):

    def __init__(self, x, y, filename, centered, speed):
        Sprite.__init__(self, x, y, filename, centered)
        self.speed = speed
        self.goal_x = x
        self.is_moving = False

    def move_to(self, x):
        self.goal_x = x
        self.is_moving = True

    def update(self):
        if(self.is_moving):
            if(self.x < self.goal_x):
                self.x = self.x + self.speed
            if(self.x > self.goal_x):
                self.x = self.x - self.speed
            if(math.fabs(self.goal_x - self.x) < self.speed):
                self.is_moving = False
            

    