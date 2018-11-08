""" Racer game """
import pygame, os, math

def main():
    """ Main function """
    # Load
    pygame.init()
    path = os.path.abspath('.') + '/'
    screen = pygame.display.set_mode((1280, 720))
    font = pygame.font.Font(path + "arial.ttf", 24)
    quit_game = False

    car = pygame.image.load(path+"images/car.png").convert_alpha()
    r_car = pygame.image.load(path+"images/car.png").convert_alpha()
    car_x = 100
    car_y = 400
    car_origin_x = -car.get_width() / 2
    car_origin_y = -car.get_height() / 2
    car_angle = 0
    car_velocity = 0

    key_up = False
    key_down = False
    key_left = False
    key_right = False

    while not quit_game:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
                if event.key == pygame.K_UP:
                    key_up = True
                if event.key == pygame.K_DOWN:
                    key_down = True
                if event.key == pygame.K_LEFT:
                    key_left = True
                if event.key == pygame.K_RIGHT:
                    key_right = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_up = False
                if event.key == pygame.K_DOWN:
                    key_down = False
                if event.key == pygame.K_LEFT:
                    key_left = False
                if event.key == pygame.K_RIGHT:
                    key_right = False

        # Update
        if key_up:
            car_velocity = car_velocity + 0.04
        if key_left:
            car_angle = car_angle - 0.5
        if key_right:
            car_angle = car_angle + 0.5
        if car_velocity > 2:
            car_velocity = 2

        car_x = car_x + car_velocity * math.cos(math.radians(car_angle))
        car_y = car_y + car_velocity * math.sin(math.radians(car_angle))
        car_velocity = car_velocity * 0.99

        # Draw
        screen.fill((0, 0, 0))

        rotated_car = pygame.transform.rotate(car, -car_angle)
        screen.blit(rotated_car, (car_x + car_origin_x, car_y + car_origin_y))

        pygame.display.update()

if __name__ == "__main__":
    main()
