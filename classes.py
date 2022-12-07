import pygame, random
import os

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
shoot = False

#load image
bullet_image = pygame.image.load("bullet.png").convert_alpha()

#list of bullets
bullets = []

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
            img = pygame.image.load("enemy_updated.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
        elif self.character == 'player':
            img = pygame.image.load("player.png").convert_alpha()
            img = pygame.transform.flip(img, True, False)
        
        self.image = pygame.transform.scale(img, (img.get_width() / 5, img.get_height() / 5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.direction = 1
        self.flip = False
        self.jump = False
        self.y_vel = 0

        self.shoot_cooldown = 0

        self.health = 1
        self.max_health = self.health

    def update(self):
        self.check_alive
        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 5

    def move(self, moving_left, moving_right):
        #Resetting the movement variables
        dy = 0
        dx = 0 

        #Assigning the movement variables if moving right or left
        if moving_left:
            dx = -self.speed
            self.direction = 1
            self.flip = False
        if moving_right:
            dx = self.speed
            self.direcion = -1
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

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown == 20
            # bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction)
            # bullet_group.add(bullet)
    
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction 

        self.flip = False 

        self.image = pygame.transform.scale(bullet_image, (bullet_image.get_width() / 10, bullet_image.get_height() / 10))

    ### added to figure out how bullet can shoot from the left, but idk how LOL
    def move(self, moving_left, moving_right):
        #Resetting the movement variables
        dy = 0
        dx = 0 

        #Assigning the movement variables if moving right or left
        if moving_left:
            dx = -self.speed
            self.direction = 1
            self.flip = False
        if moving_right:
            dx = self.speed
            self.direcion = -1
            self.flip = True
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update(self):
        #move the bullet
        self.rect.x += (self.direction * self.speed)

        #check boundaries of bullets
        if self.rect.right < 0 or self.rect.left > 1280 - 100:
            self.kill()

        # #check collision with characters
        # if pygame.sprite.spritecollide(enemy, bullet_group, False):
        #     if player.alive:
        #         player.health -= 1
        #         self.kill()


#create sprite groups
bullet_group = pygame.sprite.Group()

enemy = Person('enemy', random.randrange(850, 900), random.randrange(730, 735), 5) 
player = Person('player', 200, 705, 5)

#create screen 
status = True
while (status):
    
    clock.tick(FPS)

    draw_background()

    player.update()
    player.draw()
    player.move(moving_left, moving_right)

    enemy.update()
    enemy.draw()
    #enemy.move(moving_left, moving_right)

    # update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)

    #update player actions
    if player.alive:
        #shooting bullets
        if shoot:
            player.shoot()
            bullet = Bullet(player.rect.x + 370, player.rect.y + 340, player.direction)
            bullet_group.add(bullet)


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
        
        #Keyboard inputs movement
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                moving_left = True
            if i.key == pygame.K_d:
                moving_right = True
            if i.key == pygame.K_SPACE:
                player.jump = True
            if i.key == pygame.K_ESCAPE:
                status = False 

            #keyboard input to shoot
            if i.key == pygame.K_r:
                shoot = True
                    
            # if i.key == pygame.K_q:
            #     shoot == True
        
        #Keyboard inputs released
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_a:
                moving_left = False
            if i.key == pygame.K_d:
                moving_right = False

            #keyboard release from shoot
            if i.key == pygame.K_r:
                shoot = False 
            # if i.key == pygame.K_q:
            #     shoot == False

    

    pygame.display.update()