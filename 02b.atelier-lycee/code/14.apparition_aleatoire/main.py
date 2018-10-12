''' ##################### DEFENDER ##################### '''
import os
import pygame
import random

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
    tir_emis = False

    joueur_x = 0
    joueur_y = 200
    joueur_hauteur = 120

    ecran_hauteur = 720
    ecran_largeur = 1280

    tirs_a_effacer = []
    liste_tir = []
    random.seed()

    def creer_tir(y):
        nonlocal tir_emis
        tir = {'x': 120, 'y': y, 'vitesse': 5, 'image': pygame.image.load(path+'tir.png').convert_alpha()}
        liste_tir.append(tir)
        tir_emis = True

    def dessiner_tirs():
        for tir in liste_tir:
            ecran.blit(tir['image'], (tir['x'], tir['y']))

    def deplacer_tirs():
        for index, tir in enumerate(liste_tir):
            tir['x'] = tir['x'] + tir['vitesse']
            if tir['x'] > ecran_largeur:
                tirs_a_effacer.append(index)

    def effacer_tirs(tirs_a_effacer):
        for index in tirs_a_effacer:
            del liste_tir[index]
        tirs_a_effacer[:] = []

    liste_ennemis = []
    ennemis_a_effacer = []

    def creer_ennemis(y):
        ennemi = {'x': ecran_largeur, 'y': y, 'vitesse': -3, 'image': pygame.image.load(path+'ennemi.png').convert_alpha()}
        liste_ennemis.append(ennemi)

    def dessiner_ennemis():
        for ennemi in liste_ennemis:
            ecran.blit(ennemi['image'], (ennemi['x'], ennemi['y']))

    def deplacer_ennemis():
        for index, ennemi in enumerate(liste_ennemis):
            ennemi['x'] = ennemi['x'] + ennemi['vitesse']
            if ennemi['x'] < 0:
                ennemis_a_effacer.append(index)

    def effacer_ennemis(ennemis_a_effacer):
        for index in ennemis_a_effacer:
            del liste_ennemis[index]
        ennemis_a_effacer[:] = []

    compteur_ennemi = 0


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
                    tir_emis = False

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
        # Tirs
        if key_space and not tir_emis:
            creer_tir(joueur_y + 50)
        deplacer_tirs()
        effacer_tirs(tirs_a_effacer)
        # Ennemis
        deplacer_ennemis()
        effacer_ennemis(ennemis_a_effacer)
        compteur_ennemi = compteur_ennemi + 1
        if compteur_ennemi > 500:
            creer_ennemis(random.randint(0, ecran_hauteur - 120))
            compteur_ennemi = 0

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
        dessiner_ennemis()

        pygame.display.update()

if __name__ == "__main__":
    main()
