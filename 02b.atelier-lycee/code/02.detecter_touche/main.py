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
                    print("appui touche haut")
                if event.key == pygame.K_DOWN:
                    touche_bas = True
                    print("appui touche bas")

            if event.type == pygame.KEYUP:
                # Ajouter les touches qu'on relache ici
                if event.key == pygame.K_UP:
                    touche_haut = False
                    print("laché touche haut")
                if event.key == pygame.K_DOWN:
                    touche_bas = False
                    print("laché touche bas")


        '''
        #################### UPDATE ####################
        Update gère la logique du jeu et met à jour tout
        ce qui se passe dans le jeu
        ################################################
        '''
        # Ajouter le code Update ici




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
        ecran.blit(joueur, (0, 200))



        pygame.display.update()

if __name__ == "__main__":
    main()
