import time
import pygame

def main():
    pygame.init()
    screen, font, text = None, None, None

    load()
    update()
    draw()

    time.sleep(2)
    pygame.quit()


def load():
    global screen, font, text
    screen_size = screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Hello World")
    font = pygame.font.Font(None, 24)
    text = font.render("Hello, World.", True, (255, 126, 0))


def update():
    pass


def draw():
    global screen
    screen.blit(text, (10, 10))
    pygame.display.update()


if __name__ == "__main__":
    main()
