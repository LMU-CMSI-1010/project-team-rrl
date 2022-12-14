"""
Collaborators: Raihana Zahra, Rayane Tarazi, Lauren Campbell
About: The file that allows the game to run and change screens
"""
import pygame 
from menu import *
from mechanics import *

class Game():
    def __init__(self):
        pygame.init()
        # initializing gameplay mechanics
        self.running = True
        self.playing = False
        self.up_key = False
        self.down_key = False
        self.back_key = False
        self.start_key = False
        # identifying colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        # creating screen
        self.display_width = 1280
        self.display_height = 832
        self.display = pygame.Surface((self.display_width, self.display_height))
        self.window = pygame.display.set_mode(((self.display_width, self.display_height)))
        self.font_name = "assets/font/IBMPlexMono-Medium.ttf"
        self.mainMenu = MainMenu(self)
        self.helpMenu = helpMenu(self)
        self.quitMenu = quitMenu(self)
        self.creditsMenu = creditsMenu(self)
        self.curr_menu = self.mainMenu

    # checking for any instances of the key being pressed
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_key = True
                if event.key == pygame.K_BACKSPACE:
                    self.back_key = True
                if event.key == pygame.K_DOWN:
                    self.down_key = True
                if event.key == pygame.K_UP:
                    self.up_key = True

    # resetting the input of all the keys to false
    def resetInput(self):
        self.up_key = False
        self.down_key = False
        self.back_key = False
        self.start_key = False

    # basic text characteristics
    def drawText(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.white)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
        
    # creating game loop given the state change
    def game_loop(self):
        while self.playing:
            self.resetInput()
            if self.start_key:
                self.curr_menu.run_display = True
                self.running = False
            self.checkEvents()
            runthrough()

    def music_player(self):
        # adds music to the background on an infinite loop
        music = pygame.mixer.music.load('assets/music/background_music.mp3')
        pygame.mixer.music.play(-1)
    