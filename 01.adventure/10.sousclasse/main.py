import pygame, time, sys, math
from sprite import Sprite
from sprite_controlled import SpriteControlled

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)

    path = 'D:\\Code\\ArtFx\\Python\\python-training\\01.adventure\\07.copain\\'
    background = pygame.image.load(path+'background.png').convert()
    ground = pygame.image.load(path+'ground.png').convert()

    mouse_click = (0, 0)

    player = SpriteControlled(100, 400, 'sprite.png', 2)
    copain = Sprite(500, 400, 'copain.png')
    cursor = Sprite(0, 0, 'cursor.png')
    pygame.mouse.set_visible(False)
    collision_text = font.render("Oops, sorry.", False, (0, 0, 0))

    quit = False

    while not(quit):
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = False
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
            screen.blit(collision_text, (player.x, player.y - 100))
        cursor.draw(screen)
        
        pygame.display.update()

if __name__ == "__main__":
    main()