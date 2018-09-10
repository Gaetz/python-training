import pygame

class UiPanel:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = True
        self.color = (255, 255, 255)
        self.events = {}
        self.is_hover = False
        self.set_event("hover_in", self.on_hover_in)
        self.set_event("hover_out", self.on_hover_out)

    def set_event(self, event_type, function):
        self.events[event_type] = function

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

    def set_visible(self, value):
        self.visible = value

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))