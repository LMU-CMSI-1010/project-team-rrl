"""
testing out whether the camera can really follow the player or not
"""

import pygame
vec = pygame.math.Vector2
from abc import ABC, abstractmethod

class Camera():
    def __init__(self, player):
        self.player = player
        self.offset = vec(0,0)
        self.offset_float = vec(0,0)
        self.display_w, self.display_h = 1280, 832
        self.constant = vec(-self.display_w / 2 + player.rect.w / 2, -self.player.ground_y + 20)

    def setmethod(self, method):
        self.method = method
    
    def scroll(self):
        self.method.scroll()
    
class CamScroll(ABC):
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def scroll(self):
        pass

class Follow(CamScroll):
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)
    
    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.constant.x)
        self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.constant.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)


# loading the camera, this needs to go somewhere else
user = Player()
camera = Camera(user)
follow = Follow(camera, user)
camera.setmethod(follow)
camera.scroll

# to update window once code is moved
"""
window.blit(obstacle, (0 - camera.offset.x , 0 - camera.offset.y))
window.blit(player image, (plauer.rect.x - camera.offset.x, cat.rect.y - camera.offset.y))
"""