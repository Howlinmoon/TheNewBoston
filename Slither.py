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
fps = 10
AppleThickness = 30

direction = "right"
clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#font = pygame.font.Font(None, 25)

img = pygame.image.load('SnakeHead.png')
appleimg = pygame.image.load("apple.png")

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')
icon = pygame.image.load("apple.png")
pygame.display.set_icon(icon)

# update the entire surface
pygame.display.flip()

# pause the game
def pause():
    paused = True
    print 'Game is Paused'
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    print 'quitting from the pause routine'
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Paused",
                          black,
                          -100,
                          size="large")

        message_to_screen("Press C to continue or Q to quit.",
                          black,
                          25,
                          size="small")

        pygame.display.update()
        clock.tick(5)
        
        
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness)) #/ 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness)) #/ 10.0) * 10.0
    return randAppleX,randAppleY


# every good game needs a title screen!
def game_intro():
    intro = True
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30,
                          "small")
        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10,
                          "small")
        message_to_screen("If you run into yourself, or the edges, you die!",
                          black,
                          50,
                          "small")
        message_to_screen("Press C to play, P to pause or Q to quit.",
                          black,
                          180,
                          "small")
        pygame.display.update()
        clock.tick(15)


# drawing the snake
def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

# creating a text object for display
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()

# displaying the text object
def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf,textRect = text_objects(msg,color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

# main game loop
def gameLoop():
    global direction
    
    direction = "right"
    gameExit = False
    gameOver = False
    
    lead_x = display_width / 2
    lead_y = display_height / 2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    # generate random co-ords for the "apple" target
    randAppleX, randAppleY = randAppleGen()
    
    clock = pygame.time.Clock()

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size = "large")
            message_to_screen("Press C to play again, or Q to quit", black, 50, size = "medium")
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
                    direction = "left"
                    
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                    
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                    
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
                
                elif event.key == pygame.K_p:
                    pause()
        
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            print "You have left the game screen - the game is over!"
            gameOver = True
                    
        lead_x += lead_x_change
        lead_y += lead_y_change  
              
        gameDisplay.fill(white)
        # old drop blocky apple routine
        # pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

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
        
        # call our new fancy display score routine!
        score(snakeLength - 1)
        
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
                randAppleX, randAppleY = randAppleGen()
                snakeLength +=1
        
        clock.tick(fps)
        
        
    
    # unitialize
    pygame.quit()
    
    quit()

game_intro()
gameLoop()


