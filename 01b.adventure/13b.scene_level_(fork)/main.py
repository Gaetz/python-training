import pygame, time, sys, math
from sprite import Sprite
from sprite_controlled import SpriteControlled
from scene import Scene
from level_00 import Level00
from level_01 import Level01

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.mouse.set_visible(False)
    quit_game = False

    level00 = Level00("background.png", "ground.png")
    level01 = Level01("background.png", "ground1.png")
    scenes = {}
    scenes["level00"] = level00
    scenes["level01"] = level01
    current_scene = level00

    def change_scene(name):
        nonlocal current_scene
        current_scene = scenes[name]

    while not quit_game:
        # Inputs
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
        current_scene.inputs(events)

        # Update
        current_scene.update(change_scene)
        
        # Draw
        screen.fill((0, 0, 0))
        current_scene.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()