"""
2am testing
"""
import pygame
from gameplay import Game
# from camera import * 

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()