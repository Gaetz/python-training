""" Racer game """
import pygame
import os
import math
import time

from car import Car

def main():
    """ Main function """
    # Load
    pygame.init()
    path = os.path.abspath('.') + '/'
    screen = pygame.display.set_mode((1280, 720))
    font = pygame.font.Font(path + "arial.ttf", 24)
    quit_game = False

    key_up = False
    key_down = False
    key_left = False
    key_right = False

    car = Car(200, 300, path + "images/car.png")

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
            car.accelerate()
        if key_left:
            car.turn_left()
        if key_right:
            car.turn_right()
            
        car.update()

        # Draw
        screen.fill((0, 0, 0))

        car.draw(screen)

        pygame.display.update()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
