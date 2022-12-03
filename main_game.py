"""
screen testing
November 24, 2022
"""

# importing libraries
import pygame
from pygame.locals import *

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
image = pygame.image.load("player.png").convert()
enemy = pygame.image.load('enemy.png').convert()


# copying content from each screen
screen.blit(impstart, (0, 0))

#Classes
class Player(object): 
    #move the player across the screen, have a hitbox/range where you can shoot and kill
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_jump = False
        self.jump_count = 10

    def draw(self):
        # Initialing Color
        color = (255,0,0)
  
        # Drawing Rectangle
        pygame.draw.rect(screen, color, (self.x, self.y, 40, 40))

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.is_jump:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= self.jump_count**2 * 0.1 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10
        
        


class Enemy(object):
    #move the player across the screen, have a hitbox/range where you can shoot and kill

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0

    def draw(self):
        screen.blit(self.image,(self.x, self.y))

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

#Starting the level
user = Player(40, y - 80)
def level_start():
    screen.blit(level_background,(0,0))
    screen.blit(level_ground,(0, 832 - 40))
    user.draw() 

status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
        
        x,y = pygame.mouse.get_pos()
        if i.type == pygame.MOUSEBUTTONDOWN and 145 < x < 445 and 566 < y < 666:
            level_start()
        
        if i.type == pygame.KEYDOWN and pygame.key.get_pressed()[K_SPACE]:
                # Start to jump by setting isJump to True.
            print('yes')
            user.is_jump = True
            

    user.jump()
    clock.tick(60)
    pygame.display.update()


    #print(pygame.mouse.get_pressed()[0])
pygame.quit()