"""
Collaborators: Raihana Zahra, Rayane Tarazi, Lauren Campbell
About: main game loop that contains references to every other game file
"""
import pygame, random, os
from gameplay import Game

g = Game()

while g.running:
    g.music_player()
    g.curr_menu.display_menu()
    g.game_loop()
pygame.display.quit()
pygame.quit()
exit()
