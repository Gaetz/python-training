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

    quit_game = False
    key_a = False
    key_g = False
    key_p = False
    key_z = False
    key_s = False
    key_m = False
    key_space = False
    key_d = False
    key_t = False
    key_e = False
    key_f = False
    state = ""

    def reset_keys():
        nonlocal key_a, key_g, key_p, key_z, key_s, key_m, key_space, key_d, key_t, key_e, key_f
        key_a = key_g = key_p = key_z = key_s = key_m = key_space = key_d = key_t = key_e = key_f = False

    def change_state(new_state):
        nonlocal state
        state = new_state
        reset_keys()
        change_text(new_state)

    def change_text(state):
        nonlocal text
        if state == 'start':
            text = []
            text.append('Alors du veux créer des jeux vidéo ?')
            text.append('G pour devenir Game Designer')
            text.append('A pour devenir Artiste')
            text.append('P pour devenir Programmeur')
            text.append('Z pour devenir Producteur')

        if state == 'artiste':
            text = []
            text.append('Tu te spécialises en graphisme 2D ou en 3D ?')
            text.append('D pour 2D')
            text.append('T pour 3D')
        if state == 'artiste 2d':
            text = []
            text.append('Ca va te prendre un moment avant de devenir concept artist.')
        if state == 'artiste 3d':
            text = []
            text.append('A toi les collections de chapeaux !')
        

        if state == 'gd':
            text = []
            text.append('Tu préfères les petits jeux Smartphones ou les Grosses productions ?')
            text.append('S pour Smartphone')
            text.append('G pour Grosses production')
        if state == 'gd grosses productions':
            text = []
            text.append('Il te faudra te spécialiser au sein d\'une équipe.')
        if state == 'gd smartphone':
            text = []
            text.append('Tu vas devoir travailler seul sur plusieurs compétences.')

        if state == 'programmeur':
            text = []
            text.append('Plutôt programmeur Gameplay ou Moteur ?')
            text.append('G pour Gameplay')
            text.append('M pour Moteur')
        if state == 'programmeur gameplay':
            text = []
            text.append('Un boulot répandu et facile à trouver.')
        if state == 'programmeur moteur':
            text = []
            text.append('Un boulot assez spécifique, mais très apprécié.')

        if state == 'producteur':
            text = []
            text.append('Tu travailles en Freelance ou dans une Entreprise ?')
            text.append('F pour Freelance')
            text.append('E pour Entreprise')
        if state == 'producteur freelance':
            text = []
            text.append('La coordination de plein de gens de plein de boites !')
        if state == 'producteur entreprise':
            text = []
            text.append('La passion de la gestion d\'équipe !')
        
        
    change_state("start")
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
                if event.key == pygame.K_d:
                    key_d = True
                if event.key == pygame.K_t:
                    key_t = True
                if event.key == pygame.K_e:
                    key_e = True
                if event.key == pygame.K_f:
                    key_f = True

        # Update
        if key_space:
            change_state('start')

        if state == 'start':
            if key_a:
                change_state('artiste')
            if key_g:
                change_state('gd')                      
            if key_p:
                change_state('programmeur')
            if key_z:
                change_state('producteur')
        
        if state == 'artiste':
            if key_d:
                change_state('artiste 2d')
            if key_t:
                change_state('artiste 3d')
            
        if state == 'gd':
            if key_g:
                change_state('gd grosses productions')
            if key_s:
                change_state('gd smartphone')
        
        if state == 'programmeur':
            if key_g:
                change_state('programmeur gameplay')
            if key_m:
                change_state('programmeur moteur')

        if state == 'producteur':
            if key_f:
                change_state('producteur freelance')
            if key_e:
                change_state('producteur entreprise')
            
        
                
        # Draw
        screen.fill((0, 0, 0))

        for i in range(0, text.__len__()):
            text_surface = font.render(text[i], False, (255, 255, 255))
            screen.blit(text_surface, (10, i * 30 + 20))
        
        pygame.display.update()

if __name__ == "__main__":
    main()