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
impstart = pygame.image.load("assets/start_screen.png").convert_alpha()
level_background = pygame.image.load('background.jpeg').convert_alpha()
level_ground = pygame.image.load('road.png').convert_alpha()
player = pygame.image.load("player.png").convert_alpha()
enemy = pygame.image.load('enemy.png').convert_alpha()

# image on object
player_rect = player.get_rect(midbottom = (90, 780))


# copying content from each screen
screen.blit(impstart, (0, 0))

#### separate start screen into its own gamestate, as well as play and end screen 

#Classes
class Player(object): 
    #move the player across the screen, have a hitbox/range where you can shoot and kill
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0 
        self.score = 0
        self.hitbox = (self.x + 10, self.y + 10, 30, 40)


    def draw(self):
        screen.blit(player, player_rect)

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y
    
        # Drawing Rectangle
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 40, 40))

    def jump(self):
        self.gravity = -30
        #jump higher is a greater negative number (-100)

class Enemy(object):
    #move the player across the screen, have a hitbox/range where you can shoot and kill

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0

    def draw(self):
        screen.blit(enemy,(self.x, self.y))

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
        
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                user.jump()
            print('yes')
    
    #natural looking gravity 
    user.gravity += 1
    player_rect.y += user.gravity 

    #the floor 
    if player_rect.bottom > 600: 
        player_rect.bottom = 600

    #redraw the background after every frame from jumping         
    screen.blit(level_background,(0,0))
    screen.blit(level_ground,(0, 832 - 40))

    #redraw the player
    user.draw()

    #clock 
    clock.tick(60)
    pygame.display.update()


    #print(pygame.mouse.get_pressed()[0])
pygame.quit()