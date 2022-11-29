"""
screen testing
November 24, 2022
"""

# importing libraries
import pygame

# initializing library
pygame.init() 
x = 1280
y = 832

# creating window object and caption for window
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('shooter!')

# loading image onto surface object
impstart = pygame.image.load("assets/start_screen.png").convert()

# copying content from each screen
screen.blit(impstart, (0, 0))

pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()