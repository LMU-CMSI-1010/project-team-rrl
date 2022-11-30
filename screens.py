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
clock = pygame.time.Clock()

# loading image onto surface object
impstart = pygame.image.load("assets/start_screen.png").convert()
level_background = pygame.image.load('background.jpeg').convert()
level_ground = pygame.image.load('road.png').convert()

# copying content from each screen
screen.blit(impstart, (0, 0))

#Starting the level
def level_start():
    screen.blit(level_background,(0,0))
    screen.blit(level_ground,(0, 832 - 40))


pygame.display.flip()
clicked = False
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
        
        x,y = pygame.mouse.get_pos()
        if i.type == pygame.MOUSEBUTTONDOWN and 145 < x < 445 and 566 < y < 666:
            level_start()
            pygame.display.flip()
        

        
    clock.tick(60)


    #print(pygame.mouse.get_pressed()[0])
pygame.quit()