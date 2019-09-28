from pygame import *
from pygame.sprite import *


class Block(Sprite):
    
    falling = True
    gravity = 0
    
    
    def __init__(self, x, y, multiplier):
        Sprite.__init__(self)
        self.image = image.load("block.bmp")
        self.size = self.image.get_size()
        self.m = multiplier #shortened to m for efficiency
        self.biggerimg = pygame.transform.scale(self.image, (int(self.size[0]*self.m), int(self.size[1]*self.m)))
        self.image = self.biggerimg
        self.size = self.image.get_size()
        self.rect = self.image.get_rect().move(x, y)

    
    def update(self):
        
        if (self.falling == True):
            self.rect.y += self.gravity
            if self.gravity < 8: # 8 is Terminal Velocity. No variable required as only written once.
                self.gravity += (0.1)
            if self.rect.y >= 600 - self.size[1]:
                self.falling = False
        if self.falling == False:
            self.rect.y -= self.gravity
            if self.gravity > 0.1:
                self.gravity -= 0.1
            if self.rect.y == 20:
                self.falling = True
        if self.gravity <= 0.1 and self.falling == False:
            self.falling = True
                
        

    def getblocksize(self):
        return self.size
            
    def __repl__(self):
        return 'A Block'

        
    def popBlock(self, offset, trajectoryRight, div):
        
        #self.block = block
        self.offset = offset
        self.trajectoryRight = trajectoryRight
        self.div = div
        
        subBlock = SubBlock(self.rect.x+self.offset, self.rect.y, trajectoryRight, div)
        
        return subBlock
    
class SubBlock(Block):
    
    def __init__(self, x, y, trajectoryRight, ballscale):
        Sprite.__init__(self)
        self.image = image.load("block.bmp")
        self.size = self.image.get_size()
        self.ballscale = ballscale
        self.smallerimg = pygame.transform.scale(self.image, (int(self.size[0]/self.ballscale), int(self.size[1]/self.ballscale)))
        self.rect = self.smallerimg.get_rect().move(x, y)
        self.image = self.smallerimg
        self.size = self.image.get_size()
        self.trajectoryRight = trajectoryRight
        
    def update(self):
        
        if (self.falling == True):
            self.rect.y += self.gravity
            if self.gravity < 8:
                self.gravity += (0.1)
            if self.rect.y >= (600 - self.size[1]):
                self.falling = False
        if self.falling == False:
            self.rect.y -= self.gravity
            if self.gravity > 0.1:
                self.gravity -= 0.1
            if self.rect.y == 20:
                self.falling = True
        if self.gravity <= 0.1 and self.falling == False:
            self.falling = True
        if self.trajectoryRight == True:
            self.rect.x += 3
            if self.rect.x >= 800 - self.size[0]:
                self.trajectoryRight = False
        if self.trajectoryRight == False:
            self.rect.x -= 3
            if self.rect.x <= 0:
                self.trajectoryRight = True
        