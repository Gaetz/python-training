import pygame

class Text(object):
    def __init__(self, text):
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(text, False, (50, 200, 100))
        
    def change_text(self, text):
        self.text = self.font.render(text, False, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.text, (10, 10))