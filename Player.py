from pygame import *
from pygame.sprite import *

class Tank(Sprite):
    
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("tank.bmp").convert()
        self.rect = self.image.get_rect().move(350, 500)
        self.size = self.image.get_size()
        
    
    def moveLeft(self):
        self.rect.x -= 5
        if self.rect.x <= 0 - self.size[0]:
            self.rect.x = 800
        
    def moveRight(self):
        self.rect.x += 5
        if self.rect.x >= 800 + self.size[0]:
            self.rect.x = 1 - self.size[0] 
        
        
