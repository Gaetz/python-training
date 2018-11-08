import pygame
from sprite import Sprite

class SpriteStateful(Sprite):
    def __init__(self, x, y, filenames, centered, states, base_state):
        self.states = states
        self.filenames = filenames
        Sprite.__init__(self, x, y, filenames[0], centered)
        self.change_state(base_state)

    def change_state(self, new_state):
        index = self.states.index(new_state)
        self.surface = pygame.image.load(Sprite.path + self.filenames[index]).convert_alpha()
        self.current_state = new_state

    def notify(self, message):
        if message.type == "change_state":
            self.change_state(message.content)