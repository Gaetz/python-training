import pygame

class Sprite:

    path = 'D:\\Code\\ArtFx\\Python\\python-training\\01.adventure\\09.collision_classe\\'

    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.surface = pygame.image.load(Sprite.path + filename).convert_alpha()

    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]

    def intersects(self, sprite):
        x1, y1, w1, h1 = self.x, self.y, self.surface.get_width(), self.surface.get_height()
        x2, y2, w2, h2 = sprite.x, sprite.y, sprite.surface.get_width(), sprite.surface.get_height()
        return not(x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    
    

