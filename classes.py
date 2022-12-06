import pygame 
pygame.init()

screen = pygame.display.set_mode((1280, 832))
pygame.display.set_caption("shooter!")
clock = pygame.time.Clock()

player = pygame.image.load("player.png")
screen.blit(player, (0,0))

enemy = pygame.image.load("enemy.png")

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
        self.hitbox = (self.x + 10, self.y + 10, 30, 40)


    def draw(self):
        screen.blit(self.image,(self.x, self.y))

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

class Enemy(object):
    #move the player across the screen, have a hitbox/range where you can shoot and kill

    def __init__(self, x, y, end):
        self.x = x
        self.y = y
        self.gravity = 0
        self.end = end
        self.hitbox =  (self.x + 15, self.y + 20, 40, 52)

    def draw(self):
        screen.blit(self.image,(self.x, self.y))

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

class Obstacles(object):
    #barriers for players, will kill players if they hit

    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False

class Spike(Obstacles):

    spike = pygame.image.load("spike.png")

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y - 20, 30)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False




class Projectile(object):
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

    
