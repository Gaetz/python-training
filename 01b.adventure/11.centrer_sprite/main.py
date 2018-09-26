import pygame, time, sys, math
from sprite import Sprite
from sprite_controlled import SpriteControlled

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)

    path = 'D:\\Code\\ArtFx\\Python\\python-training\\01.adventure\\11.centrer_sprite\\'
    background = pygame.image.load(path+'background.png').convert()
    ground = pygame.image.load(path+'ground.png').convert()
    ground_height = 600 - ground.get_height()

    mouse_click = (0, 0)

    player = SpriteControlled(100, ground_height, 'sprite.png', True, 2)
    copain = Sprite(500, ground_height, 'copain.png', True)
    cursor = Sprite(0, 0, 'cursor.png', False)
    pygame.mouse.set_visible(False)
    collision_text = font.render("Oops, sorry.", False, (0, 0, 0))

    quit_game = False

    while not quit_game:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                player.move_to(mouse_click[0])

        # Update
        cursor.set_position(pygame.mouse.get_pos())
        player.update()
        
        # Draw
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 500))

        copain.draw(screen)
        player.draw(screen)
        if(player.intersects(copain)):
            screen.blit(collision_text, (player.x, player.y - 200))
        cursor.draw(screen)
        
        pygame.display.update()

if __name__ == "__main__":
    main()