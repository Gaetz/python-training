import math
from sprite import Sprite

class SpritePickable(Sprite):

    def __init__(self, x, y, filename, centered, name):
        Sprite.__init__(self, x, y, filename, centered)
        self.name = name
        self.is_picked = False

    def pick(self):
        self.is_picked = True
        return self.name

    def draw(self, screen):
        if(not(self.is_picked)):
            Sprite.draw(self, screen)
            

    


    