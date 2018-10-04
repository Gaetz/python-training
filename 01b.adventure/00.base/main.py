import pygame, time, sys

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)
    text = font.render("Hello, world :)", False, (50, 200, 100))
    key = False
    quit_game = False

    while not quit_game:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = True

        # Update
        if key:
            text = font.render("How are you ?", False, (255, 255, 255))
            quit_game = True
        
        # Draw
        screen.fill((0, 0, 0))
        screen.blit(text, (10, 10))
        pygame.display.update()

    time.sleep(2) # End program after 2 seconds

if __name__ == "__main__":
    main()