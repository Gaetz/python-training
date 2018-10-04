import pygame, time, sys

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)
    path = 'D:\\Code\\ArtFx\\Python\\python-training\\01.adventure\\02.afficher_sprite\\'
    background = pygame.image.load(path+'background.png').convert()
    spr_surface = pygame.image.load(path+'sprite.png').convert()
    spr_pos = spr_x, spr_y = 100, 400
    quit_game = False

    while not quit_game:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True

        # Update

        
        # Draw
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(spr_surface, spr_pos)
        pygame.display.update()

if __name__ == "__main__":
    main()