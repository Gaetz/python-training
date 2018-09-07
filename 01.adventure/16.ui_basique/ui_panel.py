import pygame
from ui_element import UiElement

class UiPanel(UiElement):
    def __init__(self, x, y, w, h):
        UiElement.__init__(self, x, y, w, h)
        self.color = (255, 255, 255)
        UiElement.set_event(self, "hover_in", self.on_hover_in)
        UiElement.set_event(self, "hover_out", self.on_hover_out)
        self.is_hover = False

    def on_hover_in(self):
        self.change_color((175, 175, 175))

    def on_hover_out(self):
        self.change_color((255, 255, 255))

    def change_color(self, color):
        self.color = color

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if(
            not(self.is_hover)
            and (mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)
        ):
            self.is_hover = True
            self.events["hover_in"]()
        if(
            self.is_hover
            and not(mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)
        ):
            self.is_hover = False
            self.events["hover_out"]()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))