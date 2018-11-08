import pygame

class Sprite(object):

    path = 'C:\\ArtFx\\Cours\\Python\\python-training\\01b.adventure\\29.collision_fix\\images\\'

    def __init__(self, x, y, filename, centered):
        self.x = x
        self.y = y
        self.surface = pygame.image.load(Sprite.path + filename).convert_alpha()
        self.ox = 0
        self.oy = 0
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.centered = centered
        if(centered):
            self.ox = -self.width / 2
            self.oy = -self.height


    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]

    def intersects(self, sprite):
        x1, y1, w1, h1 = self.x + self.ox, self.y + self.oy, self.width, self.height
        x2, y2, w2, h2 = sprite.x + sprite.ox, sprite.y + sprite.oy, sprite.width, sprite.height
        return not(x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)

    def draw(self, screen):
        screen.blit(self.surface, (self.x + self.ox, self.y + self.oy))

    
    

