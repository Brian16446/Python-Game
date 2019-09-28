from pygame import *
from pygame.sprite import *

class Bullets(Sprite):
    
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.playerX = x
        self.playerY = y
        self.image = image.load("bullet.bmp").convert()
        self.rect = self.image.get_rect().move(self.playerX+33, self.playerY)
    def update(self):
        self.rect.y -= 5
