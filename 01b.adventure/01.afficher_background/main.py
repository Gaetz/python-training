import pygame

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)
    path = 'D:\\Code\\ArtFx\\Python\\python-training\\01.adventure\\01.afficher_background\\'
    background = pygame.image.load(path+'background.png').convert()
    quit_game = False

    while not quit_game:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True

        # Update
        
        
        # Draw
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.display.update()

if __name__ == "__main__":
    main()