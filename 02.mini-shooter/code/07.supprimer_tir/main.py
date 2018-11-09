''' ##################### MINI SHOOTER ##################### '''
import os
import pygame

def main():


    '''
    ##################### LOAD ########################
    Load: charge les données et les variables du jeu
    ###################################################
    '''
    pygame.init()
    quit_game = False
    screen = pygame.display.set_mode((1280, 720))
    path = os.path.abspath('.') + '/'

    # Ajouter les nouvelles variables ici
    joueur = pygame.image.load(path+'joueur.png').convert_alpha()
    key_up = False
    key_down = False
    key_space = False
    tir_emis = False

    joueur_x = 0
    joueur_y = 200
    joueur_hauteur = 120

    ecran_hauteur = 720
    ecran_largeur = 1280

    tirs_a_effacer = []
    liste_tir = []

    def creer_tir(y):
        nonlocal tir_emis
        tir = {'x': 120, 'y': y, 'vitesse': 5, 'image': pygame.image.load(path+'tir.png').convert_alpha()}
        liste_tir.append(tir)
        tir_emis = True

    def dessiner_tirs():
        for tir in liste_tir:
            screen.blit(tir['image'], (tir['x'], tir['y']))

    def deplacer_tirs():
        for index, tir in enumerate(liste_tir):
            tir['x'] = tir['x'] + tir['vitesse']
            if tir['x'] > ecran_largeur:
                tirs_a_effacer.append(index)

    def effacer_tirs(bullets_to_erase):
        #for index in bullets_to_erase:
        #    del liste_tir[index]
        for index in range(len(bullets_to_erase) - 1, -1, -1):
            del liste_tir[index]
        tirs_a_effacer[:] = []


    while not quit_game:
        '''
        #################### INPUTS ######################
        Ici seront gérées les commandes du jeu

        Quand on veut ajouter des touches: il faut déclarer
        la touche avant la partie Load:

        key_espace = False

        On teste l'appui de la touche du clavier en dessous de:
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                key_espace = True

        et on testele fait qu'on relache la touche en dessous de:
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_SPACE:
                key_espace = False

        ##################################################
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
                # Ajouter les touches qu'on appuie ici
                if event.key == pygame.K_UP:
                    key_up = True
                if event.key == pygame.K_DOWN:
                    key_down = True
                if event.key == pygame.K_SPACE:
                    key_space = True
                    tir_emis = False

            if event.type == pygame.KEYUP:
                # Ajouter les touches qu'on relache ici
                if event.key == pygame.K_UP:
                    key_up = False
                if event.key == pygame.K_DOWN:
                    key_down = False
                if event.key == pygame.K_SPACE:
                    key_space = False


        '''
        #################### UPDATE ####################
        Update gère la logique du jeu et met à jour tout
        ce qui se passe dans le shooter
        ################################################
        '''
        # Ajouter le code Update ici
        if key_up:
            joueur_y = joueur_y - 5
        if key_down:
            joueur_y = joueur_y + 5
        # Limiter le déplacement
        if joueur_y < 0:
            joueur_y = 0
        if joueur_y > ecran_hauteur - joueur_hauteur:
            joueur_y = ecran_hauteur - joueur_hauteur
        # Tirs
        if key_space and not tir_emis:
            creer_tir(joueur_y + 50)
        deplacer_tirs()
        effacer_tirs(tirs_a_effacer)

        '''
        ##################### DRAW #####################
        Draw dessine ce que l'on voit à l'écran. On peut
        dessiner des surfaces ou des textes. Avant de
        dessiner on efface l'écran avec screen.fill(...)

        Pour dessiner, il faut ajouter après screen.fill(...):

        screen.blit(variable_de_ce_qu_on_dessine, (x, y))
        ################################################
        '''
        screen.fill((0, 0, 0))
        # Dessiner ici
        screen.blit(joueur, (joueur_x, joueur_y))
        dessiner_tirs()


        pygame.display.update()

if __name__ == "__main__":
    main()
