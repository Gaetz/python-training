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
    key_a = False
    key_g = False
    key_p = False
    key_z = False

    while not(quit):
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
                if event.key == pygame.K_q:
                    key_a = True
                if event.key == pygame.K_g:
                    key_g = True
                if event.key == pygame.K_p:
                    key_p = True
                if event.key == pygame.K_w:
                    key_z = True

        # Update
        if key_a:
            text = []
            text.append('Tu te spécialises en graphisme 2D ou en 3D ?')
            text.append('D pour 2D')
            text.append('T pour 3D')
        if key_g:
            text = []
            text.append('Tu préfères les petits jeux Smartphones ou les Grosses productions ?')
            text.append('S pour Smartphone')
            text.append('G pour Grosses production')
        if key_p:
            text = []
            text.append('Plutôt programmeur Gameplay ou Moteur ?')
            text.append('G pour Gameplay')
            text.append('M pour Moteur')
        if key_z:
            text = []
            text.append('Tu travailles en Freelance ou dans une Entreprise ?')
            text.append('F pour Freelance')        
            text.append('E pour Entreprise')
        
        # Draw
        screen.fill((0, 0, 0))

        for i in range(0, text.__len__()):
            text_surface = font.render(text[i], False, (255, 255, 255))
            screen.blit(text_surface, (10, i * 30 + 20))
        
        pygame.display.update()

if __name__ == "__main__":
    main()