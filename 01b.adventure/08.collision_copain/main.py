import pygame, time, sys, math

def main():

    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)

    path = 'D:\\Code\\ArtFx\\Python\\python-training\\01.adventure\\07.copain\\'
    background = pygame.image.load(path+'background.png').convert()
    ground = pygame.image.load(path+'ground.png').convert()

    mouse_click = mouse_c_x, mouse_c_y = 0, 0
    spr_surface = pygame.image.load(path+'sprite.png').convert()
    spr_x, spr_y = 100, 400
    spr_is_moving = False
    spr_speed = 2
    goal_x = 0
    
    copain_x, copain_y = 500, 400
    copain_surface = pygame.image.load(path+'copain.png').convert()
    collision_text = font.render("Oops, sorry.", False, (0, 0, 0))

    cursor = pygame.image.load(path+'cursor.png').convert_alpha() # Transparence du curseur
    pygame.mouse.set_visible(False)

    key = False
    quit_game = False

    while not quit_game:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                goal_x = mouse_click[0]
                spr_is_moving = True

        # Update
        cursor_pos = pygame.mouse.get_pos()
        if(spr_is_moving):
            if(spr_x < goal_x):
                spr_x = spr_x + spr_speed
            if(spr_x > goal_x):
                spr_x = spr_x - spr_speed
            if(math.fabs(goal_x - spr_x) < spr_speed):
                spr_is_moving = False
        
        # Draw
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 500))
        screen.blit(copain_surface, (copain_x, copain_y))
        screen.blit(spr_surface, (spr_x, spr_y))

        x1, y1, w1, h1 = spr_x, spr_y, spr_surface.get_width(), spr_surface.get_height()
        x2, y2, w2, h2 = copain_x, copain_y, copain_surface.get_width(), copain_surface.get_height()
        if(not(x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)):
            screen.blit(collision_text, (spr_x, spr_y - 100))

        screen.blit(cursor, cursor_pos)
        pygame.display.update()

if __name__ == "__main__":
    main()