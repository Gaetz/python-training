import pygame, time

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 150))
    pygame.display.update()
    time.sleep(2) # End program after 2 seconds

if __name__ == "__main__":
    main()