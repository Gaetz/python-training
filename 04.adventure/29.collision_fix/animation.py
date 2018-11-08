import pygame

class Animation:
    path = 'C:\\ArtFx\\Cours\\Python\\python-training\\01b.adventure\\29.collision_fix\\images\\'
    
    def __init__(self, frame_number, frame_speed, image):
        self.frame_number = frame_number
        self.current_frame = 0
        self.frame_speed = frame_speed
        self.counter = 0
        self.surface = pygame.image.load(Animation.path + image).convert_alpha()
        self.width, self.height = self.surface.get_width() / frame_number, self.surface.get_height()

    def update(self):
        self.counter = self.counter + 1
        if self.counter > self.frame_speed:
            self.counter = 0
            self.current_frame = (self.current_frame + 1) % self.frame_number

    def get_surface(self):
        return self.surface.subsurface(pygame.Rect(self.current_frame * self.width, 0, self.width, self.height))