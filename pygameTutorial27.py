import pygame
import time
import random

pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
blue = (0,0.255)
black = (0,0,0)

display_width = 800
display_height = 600
block_size = 20
fps = 16

font = pygame.font.SysFont(None, 25)
#font = pygame.font.Font(None, 25)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

# update the entire surface
pygame.display.flip()


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
    textSurf,textRect = text_objects(msg,color)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2 - (len (msg) / 2 * 8), display_height/2])
    textRect.center = (display_width/2), (display_height/2)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()


def gameLoop():
    
    gameExit = False
    gameOver = False
    
    lead_x = display_width / 2
    lead_y = display_height / 2
    
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    
    randAppleX = round(random.randrange(0, display_width - block_size)) #/ 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0) * 10.0
    
    clock = pygame.time.Clock()

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over, press C to play again, or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    print 'Quit event detected, quitting game'
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print 'Quit event detected, quitting game'
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
            
    #        if event.type == pygame.KEYUP:
    #            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #                lead_x_change = 0
        
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            print "You have left the game screen - the game is over!"
            gameOver = True
            
        
                    
                    
        lead_x += lead_x_change
        lead_y += lead_y_change  
        
        
              
        gameDisplay.fill(white)
        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        # snake collision detection
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                # collision detected
                print "Snake hit itself!"
                gameOver = True
        
        
        snake(block_size, snakeList)
        pygame.display.update()
        
        # old crossover detection code
#         if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
#             if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
#                 randAppleX = round(random.randrange(0, display_width - block_size)) #/ 10.0) * 10.0
#                 randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0) * 10.0
#                 snakeLength +=1
        
        # new crossover detection code
        if (lead_x > randAppleX and lead_x < randAppleX+AppleThickness) or (lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness):
            if (lead_y > randAppleY and lead_y < randAppleY+AppleThickness) or (lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness):
                randAppleX = round(random.randrange(0, display_width - block_size)) #/ 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0) * 10.0
                snakeLength +=1
        
        clock.tick(fps)
        
        
    
    # unitialize
    pygame.quit()
    
    quit()

gameLoop()


