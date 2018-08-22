import pygame

screen, font = None, None
quit_game, key = False, False

def main():
    pygame.init()
    load()
    while not(quit_game):
        process_input()
        update()
        draw()

    pygame.quit()


def load():
    global screen, font, text
    screen_size = screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Adventure")
    font = pygame.font.Font(None, 24)

def process_input():
    global quit_game, key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            key = True

def update():
    pass

def draw():
    screen.fill((0, 0, 0))
    #screen.blit(text, (10, 10))
    pygame.display.update()


if __name__ == "__main__":
    main()
