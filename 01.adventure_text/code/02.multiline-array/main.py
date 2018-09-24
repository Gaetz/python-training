import pygame, sys

def main():

    # Load
    pygame.init()
    path = "c:\\ArtFx\\Cours\\Python\\python-training\\01.adventure_text\\code\\00.start\\"
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(path + "arial.ttf", 24)

    text = []
    text.append('Alors du veux créer des jeux vidéo ?')
    text.append('G pour devenir Game Designer')
    text.append('A pour devenir Artiste')
    text.append('P pour devenir Programmeur')
    text.append('Z pour devenir Producteur')

    quit = False
    
    while not(quit):
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True

        # Update
        
        # Draw
        screen.fill((0, 0, 0))

        for i in range(0, text.__len__()):
            text_surface = font.render(text[i], False, (255, 255, 255))
            screen.blit(text_surface, (10, i * 30 + 20))
        
        pygame.display.update()

if __name__ == "__main__":
    main()