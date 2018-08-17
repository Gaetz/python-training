import pygame
import time

pygame.init()
screen_size = screen_width, screen_height = 800, 600
screen = pygame.display.set_mode(screen_size)

font = pygame.font.Font(None, 24)
text = font.render("Hello, World.", True, (255, 126, 0))

screen.blit(text, (10, 10))
pygame.display.flip()

time.sleep(2)

pygame.quit()


