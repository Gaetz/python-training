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
    #text.append('A pour devenir Artiste')
    text.append('P pour devenir Programmeur')
    #text.append('Z pour devenir Producteur')

    quit_game = False
    key_a = False
    key_g = False
    key_p = False
    key_z = False
    key_s = False
    key_m = False
    key_space = False
    state = "start"

    while not quit_game:
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
                if event.key == pygame.K_COLON:
                    key_m = True
                if event.key == pygame.K_s:
                    key_s = True
                if event.key == pygame.K_SPACE:
                    key_space = True

        # Update
        if state == 'start':
            if key_a:
                text = []
                text.append('Tu te spécialises en graphisme 2D ou en 3D ?')
                text.append('D pour 2D')
                text.append('T pour 3D')
                state = 'artiste'            
            
            if key_g:
                text = []
                text.append('Tu préfères les petits jeux Smartphones ou les Grosses productions ?')
                text.append('S pour Smartphone')
                text.append('G pour Grosses production')
                state = 'gd'                        
            
            if key_p:
                text = []
                text.append('Plutôt programmeur Gameplay ou Moteur ?')
                text.append('G pour Gameplay')
                text.append('M pour Moteur')
                state = 'programmeur'
            
            if key_z:
                text = []
                text.append('Tu travailles en Freelance ou dans une Entreprise ?')
                text.append('F pour Freelance')        
                text.append('E pour Entreprise')
                state = 'producteur'                                    
            
        if state == 'gd':
            if key_g:
                text = []
                text.append('Il te faudra te spécialiser au sein d\'une équipe.')
                state = 'gd grosses productions'            
            if key_s:
                text = []
                text.append('Tu vas devoir travailler seul sur plusieurs compétences.')
                state = 'gd smartphone'                        
        
        if state == 'programmeur':
            if key_g:
                text = []
                text.append('Un boulot répandu et facile à trouver.')
                state = 'programmeur gameplay'            
            if key_m:
                text = []
                text.append('Un boulot assez spécifique, mais très apprécié.')
                state = 'programmeur moteur'                        
                
            
        
        # Draw
        screen.fill((0, 0, 0))

        for i in range(0, text.__len__()):
            text_surface = font.render(text[i], False, (255, 255, 255))
            screen.blit(text_surface, (10, i * 30 + 20))
        
        pygame.display.update()

if __name__ == "__main__":
    main()