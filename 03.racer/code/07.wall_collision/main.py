""" Racer game """
import pygame
import os
import math
import time

from car import Car
from track import Track

def main():
    """ Main function """
    # Load
    pygame.init()
    path = os.path.abspath('.') + '/'
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(path + "arial.ttf", 24)
    quit_game = False

    key_up = False
    key_down = False
    key_left = False
    key_right = False
    key_z = False
    key_q = False
    key_s = False
    key_d = False

    car = Car(60, 300, path + "images/car.png")
    car2 = Car(500, 300, path + "images/car-alt.png")
    track = Track()

    dt = 60 / 1000
    clock = pygame.time.Clock()
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
                if event.key == pygame.K_w:
                    key_z = True
                if event.key == pygame.K_a:
                    key_q = True
                if event.key == pygame.K_s:
                    key_s = True
                if event.key == pygame.K_d:
                    key_d = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_up = False
                if event.key == pygame.K_DOWN:
                    key_down = False
                if event.key == pygame.K_LEFT:
                    key_left = False
                if event.key == pygame.K_RIGHT:
                    key_right = False
                if event.key == pygame.K_w:
                    key_z = False
                if event.key == pygame.K_a:
                    key_q = False
                if event.key == pygame.K_s:
                    key_s = False
                if event.key == pygame.K_d:
                    key_d = False

        # Update
        # - Player 1
        if key_up:
            car.accelerate()
        if key_left:
            car.turn_left(dt)
        if key_right:
            car.turn_right(dt)
            
        car.update(dt)

        # - Player 2
        if key_z:
            car2.accelerate()
        if key_q:
            car2.turn_left(dt)
        if key_d:
            car2.turn_right(dt)
            
        car2.update(dt)

        # Draw
        screen.fill((0, 0, 0))

        track.draw(screen)
        car.draw(screen)
        car2.draw(screen)

        pygame.display.update()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
