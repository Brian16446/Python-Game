from pygame import *
from pygame.sprite import *
import time
from Blocks import *
from Player import *
from Bullets import Bullets




pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
WHITE = (255,255,255)
BLACK = (0,0,0)
pygame.display.set_caption('BriGame')
gameDisplay.fill(BLACK)
FPS = 60
clock = pygame.time.Clock()
levelCount = 0



def levelComplete(gameCompleted):
    
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    if not gameCompleted:
        textSurface = myfont.render('LEVEL COMPLETE. PRESS W TO GO TO NEXT LEVEL', False, (WHITE))
    elif gameCompleted:
        textSurface = myfont.render('YOU HAVE COMPLETED THE GAME!!', False, (WHITE))
    gameDisplay.blit(textSurface, (15,50))

def getBlockDiv(blockHeight):
    
    if blockHeight <= 400 and blockHeight > 200:
        return 0.5
    elif blockHeight <= 200 and blockHeight > 100:
        return 1
    elif blockHeight <= 100 and blockHeight > 50:
        return 2
    elif blockHeight <= 50 and blockHeight > 25:
        return 4
    elif blockHeight <= 25:
        return 8

def replay():
    
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textSurface = myfont.render('YOU LOSE PRESS Y TO RESTART OR Q TO QUIT', False, (WHITE))
    gameDisplay.blit(textSurface, (45,50))
    
    replay = True
    while not replay:
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    main()

def loadLevel(levelCount):
    
    
    level1 = [Block(200,20,0.5), Block(40,400,1)]
    level2 = [Block(500,20,2), Block(40,300,1)]
    level3 = [Block(200, 400, 1), Block(460, 400, 1), Block(320, 20, 1)]
    level4 = [Block(500,20,2), Block(40,400,1), Block(100, 10, 0.5)]
    
    """
    level1 = [Block(200,20,0.5)]        # TEST LEVELS
    level2 = [Block(500,20,0.5)]        # MAKE IT EASIER TO REACH END TO TEST LATER LEVELS
    level3 = [Block(200, 400, 0.5)]     # WITHOUT HAVING TO PLAY THROUGH THE GAME
    level4 = [Block(500,20,0.5)]        # JUST UNCOMMENT AND COMMENT OUT THE ACTUAL LEVELS
    """
    
    levels = [level1, level2, level3, level4]
    
    if levelCount < len(levels):
        main(levels[levelCount], len(levels))


def main(listBlocks, numOfLevels):

    gameRunning = True
    blockCount = len(listBlocks)
    player = Tank()
    playerSprite = Group(player)
    all_blocks = Group()
    i = 0
    while i < len(listBlocks):
        all_blocks.add(listBlocks[i]) #Grouping all the starting blocks into a group
        i += 1
    all_bullets = Group()
    playerAlive = True
    levelDefeated = False
    global levelCount
    
    while(gameRunning):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit
                    quit()
                if event.key == pygame.K_y:
                    loadLevel(levelCount)
            if (playerAlive == True):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullets(player.rect.x, player.rect.y)
                        all_bullets.add(bullet)
                        #bulletFired = True
            if (levelDefeated):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        #global levelCount
                        levelCount += 1
                        loadLevel(levelCount)
        for c, block in enumerate(listBlocks):
            if (spritecollideany(block, all_bullets, collided = None)):
                blockHeight = listBlocks[c].rect[3]
                div = getBlockDiv(blockHeight)
                if (groupcollide(all_bullets, all_blocks, True, True)):
                    if (div != 8):
                        subBlock = listBlocks[c].popBlock(100, True, div)
                        subBlock2 = listBlocks[c].popBlock(0, False, div)   
                        all_blocks.add(subBlock, subBlock2)
                        listBlocks.extend([subBlock, subBlock2])
                        blockCount += 2
                    del listBlocks[c]
                    blockCount -= 1                                          
                
        if groupcollide(playerSprite, all_blocks, True, False):
            playerAlive = False
            replay()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.moveLeft()
        if keys[pygame.K_d]:
            player.moveRight()
        print (blockCount)
        if blockCount == 0:
            levelDefeated = True
            if levelCount < numOfLevels:
                gameCompleted = False
            if levelCount >= numOfLevels:
                gameCompleted = True
            levelComplete(gameCompleted)
            

            
    
        all_bullets.draw(gameDisplay)
        playerSprite.draw(gameDisplay)
        all_blocks.draw(gameDisplay)
        playerSprite.update()
        all_blocks.update()
        all_bullets.update()
        clock.tick(FPS)
        pygame.display.update()
        gameDisplay.fill(BLACK)
        
        if not playerAlive:
            replay()
        

    pygame.quit
    quit()

# Function call to start the game.
loadLevel(levelCount)
