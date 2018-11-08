import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp
from scene import Scene

class Level01(Scene):
    
    def __init__(self, background_file, ground_file):
        Scene.__init__(self, background_file, ground_file)
        _, screen_h = pygame.display.get_surface().get_size()
        ground_height = screen_h - self.ground.surface.get_height()
        self.ground.y = ground_height
        self.player = SpriteControlled(10, ground_height, 'sprite.png', True, 2)
        self.cursor = Sprite(0, 0, 'cursor.png', False)
        self.warp = Warp(680, 0, 'warp.png', False, "level00")
        self.warp.y = ground_height - self.warp.surface.get_height() / 2

    def load(self):
        pass

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                self.player.move_to(mouse_click[0])

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.player.update()
        if self.player.intersects(self.warp):
            change_scene(self.warp.to_scene)

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        self.warp.draw(screen)
        self.player.draw(screen)
        self.cursor.draw(screen)
    