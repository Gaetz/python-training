""" Racer game """
import pygame, os

def main():
    """ Main function """
    # Load
    pygame.init()
    path = os.path.abspath('.') + '/'
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(path + "arial.ttf", 24)
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
        screen.fill((0, 0, 150))
        pygame.display.update()

if __name__ == "__main__":
    main()
