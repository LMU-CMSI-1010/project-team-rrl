import pygame, random
pygame.init()

screen = pygame.display.set_mode((1280, 832))
pygame.display.set_caption("shooter!")

clock = pygame.time.Clock() 
FPS = 60 

#Game variables
GRAVITY = 0.75

#Defining player movement variables
moving_left = False
moving_right = False

#Define colors
BG = (144, 201, 120)
RED = (255, 0, 0)
def draw_background():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 832 - 60), (1280, 832 - 60))

class Person(pygame.sprite.Sprite):
    #move the player across the screen, have a hitbox/range where you can shoot and kill

    def __init__(self, character,  x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.character = character
        self.alive = True
        
        if self.character == 'enemy':
            img = pygame.image.load("enemy.png").convert_alpha()
        elif self.character == 'player':
            img = pygame.image.load("player.png").convert_alpha()
            img = pygame.transform.flip(img, True, False)
        
        self.image = pygame.transform.scale(img, (img.get_width() / 5, img.get_height() / 5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.direc = 1
        self.flip = False
        self.jump = False
        self.y_vel = 0

    
    def move(self, moving_left, moving_right):
        #Resetting the movement variables
        dy = 0
        dx = 0 

        #Assigning the movement variables if moving right or left
        if moving_left:
            dx = -self.speed
            self.direc = 1
            self.flip = False
        if moving_right:
            dx = self.speed
            self.direc = -1
            self.flip = True
        
        #Jump
        if self.jump:
            self.y_vel = -11
            self.jump = False
        #Make guy come down with gravity
        self.y_vel += GRAVITY
        if self.y_vel > 10:
            self.y_vel 
        dy += self.y_vel 
        
        #Checking with floor
        if self.rect.bottom + dy > 832 - 60:
            dy = 832-60 - self.rect.bottom

        #update position
        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


enemy = Person('player', random.randrange(300, 800), random.randrange(200, 600), 5 )

#create screen 
status = True
while (status):
    
    clock.tick(FPS)
    draw_background()
    enemy.draw()
    enemy.move(moving_left, moving_right)


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
        
        #Keyboard inputs
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                moving_left = True
                print(moving_left)
            if i.key == pygame.K_d:
                moving_right = True
            if i.key == pygame.K_w and enemy.alive:
                enemy.jump = True
            if i.key == pygame.K_ESCAPE:
                status = False 
        
        #Keyboard inputs released
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_a:
                moving_left = False
            if i.key == pygame.K_d:
                moving_right = False 

    

    pygame.display.update()
