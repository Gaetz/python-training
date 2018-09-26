import pygame, sys

def main():

    # Load
    pygame.init()
    path = "c:\\ArtFx\\Cours\\Python\\python-training\\01.adventure_text\\code\\00.start\\"
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(path + "arial.ttf", 24)
    text = font.render("Alors tu veux créer des jeux videos ?\n G pour devenir Game Designer\n P pour devenir Programmeur\n", False, (0, 0, 0))
    quit_game = False

    while not quit_game:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True

        # Update
        
        # Draw
        screen.fill((0, 0, 150))
        screen.blit(text, (10, 10))
        pygame.display.update()

if __name__ == "__main__":
    main()