"""
Collaborators: Raihana Zahra, Rayane Tarazi, Lauren Campbell
About: File with the two main classes(Bullet and Person) as well as a while loop that is able to run the main game 
"""
import pygame, random, gameplay
import os
from camera import Camera, Follow

pygame.init()
def runthrough():

    #sets up screen with caption for screen
    screen = pygame.display.set_mode((1280, 832))
    pygame.display.set_caption("shooter!")

    #clock for time
    clock = pygame.time.Clock() 
    FPS = 60 

    #global game variables
    GRAVITY = 0.75

    # defining player movement variables
    moving_left = False
    moving_right = False
    shoot = False

    #load image of bullet into game
    bullet_image = pygame.image.load("assets/weapons/bullet.png").convert_alpha()

    #real background and ground
    level_background = pygame.image.load('assets/screens/background.png').convert_alpha()

    #draws background of screen 
    def draw_background():
        screen.blit(level_background, (0,0))

    class Person(pygame.sprite.Sprite):
        #move the player across the screen, have a hitbox/range where you can shoot and kill

        def __init__(self, character,  x, y, speed):
            pygame.sprite.Sprite.__init__(self)
            self.speed = speed
            self.groundy = y
            self.character = character
            self.alive = True
            self.jumps = 2
            
            #Checks whether to use the enemy image or the player image depending on user input
            if self.character == 'enemy':
                img = pygame.image.load("assets/characters/new_enemy.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width(), img.get_height()))
            elif self.character == 'player':
                img = pygame.image.load("assets/characters/female_character.png").convert_alpha()
                img = pygame.transform.flip(img, True, False)
            
            self.image = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            self.rect = self.image.get_rect()
            self.rect.x = 600
            self.rect.y = 832 + 60 

            self.direction = 1
            self.flip = False
            self.jump_count = 3 
            self.jump = False
            self.y_vel = 0

            self.shoot_cooldown = 0

            self.health = 1
            self.max_health = self.health
            
            #enemy specific variables:
            self.move_counter = 0
            self.idling = False
            self.idling_counter = 0 

        #Makes sure the player is alive
        def update(self):
            self.check_alive

        def move(self, moving_left, moving_right):
            #resetting the movement variables
            dy = 0
            dx = 0 

            #assigning the movement variables if moving right or left
            if moving_left:
                dx = -self.speed
                self.direction = 1
                self.flip = False
            if moving_right:
                dx = self.speed
                self.direcion = -1
                self.flip = True
            
            #jumping method for player
            if self.jump and 0 < self.jumps <=2:
                self.y_vel = -11
                self.jump = False
                self.jumps -= 1
            
            if self.jumps == 0 and self.rect.bottom == 832-60:
                self.jumps = 2

                
            #makes player come down with gravity
            self.y_vel += GRAVITY
            if self.y_vel > 10:
                self.y_vel 
            dy += self.y_vel

            #checking collision with floor
            if self.rect.bottom + dy > 832 - 60:
                dy =  832-60 - self.rect.bottom

            #update player position
            self.rect.x += dx
            self.rect.y += dy

        #method to shoot bullets from player
        def shoot(self):
            bullet = Bullet(self.rect.x + 495, self.rect.y + 370, self.direction)
            bullet_group.add(bullet)
            pygame.time.wait(100)

        #used for enemy movement
        def ai(self):
            if self.alive and player.alive:
                if self.idling == False and random.randint(1, 100) == 1:
                    self.idling = True
                    self.idling_counter = 50
                
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = False
                    else:
                        ai_moving_right = True
                    
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.move_counter += 1

                    if self.move_counter > 80 :
                        self.direction *= -1
                        self.move_counter *= -1  
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        #checks whether enemy or player is still alive
        def check_alive(self):
            if self.health <= 0:
                self.health = 0
                self.speed = 0
                self.alive = False
        
        #flips the image of player/enemy if it is turned to the right or left 
        def draw(self):
            screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    class Bullet(pygame.sprite.Sprite):
        #Initializes the bullet, giving it an x and y as well as a direction
        def __init__(self, x, y, direction):
            pygame.sprite.Sprite.__init__(self)
            self.speed = 20
            self.image = bullet_image
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
            self.direction = direction 
            self.flip = False
             
            self.image = pygame.transform.scale(bullet_image, (bullet_image.get_width() / 10, bullet_image.get_height() / 10))

        def update(self):
            #moves the bullet in the direction of the player 
            if player.flip:
                self.flip = True
                self.rect.x += (self.direction * self.speed)
            elif player.flip == False:
                self.flip = False
                self.rect.x -= (self.direction * self.speed)

            #check boundaries of bullets
            if self.rect.right < 0 or self.rect.left > 1280 - 45:
                self.kill()

            #check collision with characters --> After multiple different attempts we were unable to get the collision to work as a group
            # if pygame.sprite.spritecollide(player, bullet_group, False):
            #     if player.alive:
            #         self.kill()
            # if pygame.sprite.spritecollide(enemy, bullet_group, False):
            #     if enemy.alive:
            #         self.kill()    


    #create sprite groups
    bullet_group = pygame.sprite.Group()

    # enemy = Person('enemy', random.randrange(880, 890), random.randrange(720, 725), 5) 
    enemy = Person('enemy', 600, 832 - 60, 5) 
    player = Person('player', 200, 832 - 60, 5)

    #loading camera in game
    user = player
    camera = Camera(player)
    follow = Follow(camera, user)
    camera.setmethod(follow)

    #create screen 
    status = True
    while (status):
        
        clock.tick(FPS)

        #calls draw background function and draws background
        draw_background()
        
        #Spawns player
        player.update()
        player.draw()
        player.move(moving_left, moving_right)
        
        #Spawns enemy
        enemy.ai() 
        enemy.update()
        enemy.draw()

        # update and draw groups
        bullet_group.update()
        bullet_group.draw(screen)

        #update player actions
        if player.alive:
            #shoots bullets from player
            if shoot:
                player.shoot()

        for i in pygame.event.get():
            #Checks if the player quites
            if i.type == pygame.QUIT:
                status = False
            
            #Keyboard inputs movement
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_a:
                    moving_left = True
                if i.key == pygame.K_d:
                    moving_right = True
                
                if i.key == pygame.K_SPACE or i.key == pygame.K_w:
                    player.jump = True
                    player.jump_count -= 1 
                
                #Allows the player to also use escape to quit
                if i.key == pygame.K_ESCAPE:
                    status = False 

                #keyboard input to shoot
                if i.key == pygame.K_r:
                    shoot = True
            
            #Keyboard inputs released
            if i.type == pygame.KEYUP:
                if i.key == pygame.K_a:
                    moving_left = False
                if i.key == pygame.K_d:
                    moving_right = False

                #keyboard release from shoot
                if i.key == pygame.K_r:
                    shoot = False 

                    if player.jump_count == 0:
                            player.jump = False

        pygame.display.update()