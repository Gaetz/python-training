''' ##################### DEFENDER ##################### '''
import os
import pygame

def main():


    '''
    ##################### LOAD ########################
    Load: charge les données et les variables du jeu
    ###################################################
    '''
    pygame.init()
    fin_du_jeu = False
    ecran = pygame.display.set_mode((1280, 720))
    path = os.path.abspath('.') + '/'

    # Ajouter les nouvelles variables et fonctions ici
    joueur = pygame.image.load(path+'joueur.png').convert_alpha()
    touche_haut = False
    touche_bas = False
    key_space = False
    joueur_x = 0
    joueur_y = 200
    joueur_hauteur = 120

    ecran_hauteur = 720
    ecran_largeur = 1280

    liste_tir = []

    def creer_tir(y):
        tir = { 'x': 120, 'y': y, 'vitesse': 5, 'image': pygame.image.load(path+'tir.png').convert_alpha() }
        liste_tir.append(tir)

    def dessiner_tirs():
        for tir in liste_tir:
            ecran.blit(tir['image'], (tir['x'], tir['y']))

    while not fin_du_jeu:
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
                fin_du_jeu = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fin_du_jeu = True
                # Ajouter les touches qu'on appuie ici
                if event.key == pygame.K_UP:
                    touche_haut = True
                if event.key == pygame.K_DOWN:
                    touche_bas = True
                if event.key == pygame.K_SPACE:
                    key_space = True

            if event.type == pygame.KEYUP:
                # Ajouter les touches qu'on relache ici
                if event.key == pygame.K_UP:
                    touche_haut = False
                if event.key == pygame.K_DOWN:
                    touche_bas = False
                if event.key == pygame.K_SPACE:
                    key_space = False


        '''
        #################### UPDATE ####################
        Update gère la logique du jeu et met à jour tout
        ce qui se passe dans le jeu
        ################################################
        '''
        # Ajouter le code Update ici
        if touche_haut:
            joueur_y = joueur_y - 5
        if touche_bas:
            joueur_y = joueur_y + 5
        # Limiter le déplacement
        if joueur_y < 0:
            joueur_y = 0
        if joueur_y > ecran_hauteur - joueur_hauteur:
            joueur_y = ecran_hauteur - joueur_hauteur
        # Tir
        if key_space:
            creer_tir(joueur_y)


        '''
        ##################### DRAW #####################
        Draw dessine ce que l'on voit à l'écran. On peut
        dessiner des surfaces ou des textes. Avant de
        dessiner on efface l'écran avec ecran.fill(...)

        Pour dessiner, il faut ajouter après ecran.fill(...):

        ecran.blit(variable_de_ce_qu_on_dessine, (x, y))
        ################################################
        '''
        ecran.fill((0, 0, 0))
        # Dessiner ici
        ecran.blit(joueur, (joueur_x, joueur_y))
        dessiner_tirs()


        pygame.display.update()

if __name__ == "__main__":
    main()
