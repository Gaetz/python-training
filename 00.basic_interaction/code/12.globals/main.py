import pygame, time, sys

def main():
    pygame.init()

    load()
    while not(quit):
        inputs()
        update()
        draw()

    time.sleep(2) # End program after 2 seconds

def load():
    global screen, font, text, key, quit
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)
    text = font.render("Hello, world :)", False, (50, 200, 100))
    key = False
    quit = False

def inputs():
    global key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = True 
            
def update():
    global key, text, font, quit
    if key:
        text = font.render("How are you ?", False, (255, 255, 255))
        quit = True

def draw():
    global screen, text
    screen.fill((0, 0, 150))
    screen.blit(text, (10, 10))
    pygame.display.update()

    

if __name__ == "__main__":
    main()