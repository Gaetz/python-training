import time
import pygame, sys

def main():
    pygame.init()
    screen, font, text = None, None, None
    quit = False

    load()
    while not(quit):
        update()
        draw()

    pygame.quit()


def load():
    global screen, font, text
    screen_size = screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Hello World")
    font = pygame.font.Font(None, 24)
    text = font.render("Hello, World.", True, (255, 126, 0))

def update():
    global text, font, quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            text = font.render("How are you?", True, (255, 255, 255))

def draw():
    global screen
    screen.fill((0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.update()


if __name__ == "__main__":
    main()
