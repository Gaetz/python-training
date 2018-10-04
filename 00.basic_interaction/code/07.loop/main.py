import pygame, time

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 150))

    font = pygame.font.Font(None, 24)
    text = font.render("Hello, world :)", False, (50, 200, 100))
    screen.blit(text, (10, 10))

    key = False
    quit_game = False
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = True
        if key:
            text = font.render("How are you ?", False, (255, 255, 255))
            screen.blit(text, (10, 10))
            quit_game = True
        pygame.display.update()

    time.sleep(2) # End program after 2 seconds
    
if __name__ == "__main__":
    main()