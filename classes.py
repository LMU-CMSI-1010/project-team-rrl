import pygame 
pygame.init()

screen = pygame.display.set_mode((1280, 832))
pygame.display.set_caption("shooter!")
clock = pygame.time.Clock()

player = pygame.image.load("Desktop/CMSI1010/project-team-rrl-raihana-rayane-lauren/player.png")
screen.blit(player, (0,0))

enemy = pygame.image.load("Desktop/CMSI1010/project-team-rrl-raihana-rayane-lauren/enemy.png")


#create screen 
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

class Player(object): 
    #move the player across the screen, have a hitbox/range where you can shoot and kill
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0 
        self.score = 0

    def draw(self):
        screen.blit(self.image,(self.x, self.y))

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

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

    


