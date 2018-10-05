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
    player = pygame.image.load(path+'joueur.png').convert_alpha()
    key_up = False
    key_down = False
    joueur_x = 0
    joueur_y = 200

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

            if event.type == pygame.KEYUP:
                # Ajouter les touches qu'on relache ici
                if event.key == pygame.K_UP:
                    key_up = False
                if event.key == pygame.K_DOWN:
                    key_down = False


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
        screen.blit(player, (joueur_x, joueur_y))



        pygame.display.update()

if __name__ == "__main__":
    main()
