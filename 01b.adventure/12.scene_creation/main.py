import pygame, time, sys, math
from sprite import Sprite
from sprite_controlled import SpriteControlled
from scene import Scene

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.mouse.set_visible(False)

    #copain = Sprite(500, 400, 'copain.png', True)
    # font = pygame.font.Font(None, 24)
    #collision_text = font.render("Oops, sorry.", False, (0, 0, 0))

    level00 = Scene("level00", "background.png", "ground.png")
    current_scene = level00

    quit_game = False

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
        current_scene.update()
        
        # Draw
        screen.fill((0, 0, 0))
        current_scene.draw(screen)
        
        #copain.draw(screen)
        #if(player.intersects(copain)):
        #    screen.blit(collision_text, (player.x, player.y - 100))
        #cursor.draw(screen)
        
        pygame.display.update()

if __name__ == "__main__":
    main()