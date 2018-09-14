import pygame
from ui_element import UiElement

class UiPanel(UiElement):
    def __init__(self, x, y, w, h):
        UiElement.__init__(self, x, y, w, h)
        self.color = (255, 255, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))