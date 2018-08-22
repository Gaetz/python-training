import pygame, time, sys
from game_state import GameState
from text import Text

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    state = GameState()
    text = Text("Hello, world :)")

    while not(state.quit):
        inputs(state)
        update(state, text)
        draw(screen, text)

    time.sleep(2) # End program after 2 seconds

def inputs(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            state.key = True 
            
def update(state, text):
    if state.key:
        text.change_text("How are you ?")
        state.quit = True

def draw(screen, text):
    screen.fill((0, 0, 150))
    text.draw(screen)
    pygame.display.update()

if __name__ == "__main__":
    main()