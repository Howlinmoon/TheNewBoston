import time
import pygame
import random

# Pygame Tutorial #77

pygame.init()

white = (255,255,255)
red = (200,0,0)
light_red = (255,0,0)

green = (34,177,76)
light_green = (0,255,0)

blue = (0,0.255)
black = (0,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)


ground_height = 35

display_width = 800
display_height = 600
block_size = 20
fps = 10
AppleThickness = 30

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5



#font = pygame.font.Font(None, 25)

#img = pygame.image.load('SnakeHead.png')
#appleimg = pygame.image.load("apple.png")
#icon = pygame.image.load("apple.png")
#pygame.display.set_icon(icon)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')


# update the entire surface
pygame.display.flip()



# pause the game
def pause():
    paused = True
    print 'Game is Paused'
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue or Q to quit.",black,25,size="small")

    pygame.display.update()

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
                    
        # gameDisplay.fill(white)
        clock.tick(5)
        
        
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

# creating a text object for display
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()


def text_to_button (msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf,textRect = text_objects(msg, color, size)
    textRect.center = (buttonx + (buttonwidth / 2), buttony + (buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

# displaying the text object
def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf,textRect = text_objects(msg,color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def tank(x,y,turPos):
    # ensure our parameters are ints
    x = int(x)
    y = int(y)
    
    possibleTurrets = [(x-27, y -2),
                       (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-15),
                       (x-15, y-17),
                       (x-13, y-19),
                       (x-11, y-21)
                       ]
    
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight) )
    
    # turret
    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)
    
    # draw some red wheels
    startX = 15
    for number in range(7):
        pygame.draw.circle(gameDisplay, red, (x-startX, y+20), wheelWidth)
        startX -= 5
    
    return possibleTurrets[turPos]


def enemy_tank(x, y, turPos):
    # ensure our parameters are ints
    x = int(x)
    y = int(y)
    
    possibleTurrets = [(x+27, y -2),
                       (x+26, y-5),
                       (x+25, y-8),
                       (x+23, y-12),
                       (x+20, y-14),
                       (x+18, y-15),
                       (x+15, y-17),
                       (x+13, y-19),
                       (x+11, y-21)
                       ]
    
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight) )
    
    # turret
    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)
    
    # draw some red wheels
    startX = 15
    for number in range(7):
        pygame.draw.circle(gameDisplay, red, (x-startX, y+20), wheelWidth)
        startX -= 5
    
    return possibleTurrets[turPos]



# Display a controls help screen
def game_controls():
    gcont = True
    while gcont:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Controls",green,-100,"large")
        message_to_screen("Fire: Spacebar",black,-30,"small")
        message_to_screen("Move Turret: Up and Down arrows",black,10,"small")
        message_to_screen("Move Tank: Left and Right arrows",black,50,"small")
        message_to_screen("Pause: P",black,110,"small")

        
        button("Play", 150,500, 100, 50, green, light_green, action = "play")
        #button("Intro", 350,500, 100, 50, yellow, light_yellow, action = "intro")
        button("Quit", 550,500, 100, 50, red, light_red, action = "quit")
        
        pygame.display.update()
        clock.tick(15)



# Button Handling
def button (text, x, y, width, height, inactive_color, active_color, action = None):
    mousePointer = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+width > mousePointer[0] > x and y+height > mousePointer[1] > y:
        if click[0] == 1 and action != None:
            print "You clicked ",text
            if action == "quit":
                pygame.quit()
                quit()
                
            elif action == "controls":
                game_controls()
            
            elif action == "play":
                gameLoop()
            
            elif action == "intro":
                game_intro()
                
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


# Draw a barrier
def barrier(xlocation, randomHeight, barrier_width):
    
    pygame.draw.rect(gameDisplay, black, [xlocation, display_height - randomHeight, barrier_width, randomHeight])


def explosion(x, y, size=50):
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        startPoint = x,y
        colorChoices = [red, light_red, yellow, light_yellow]
        magnitude = 1
        while magnitude < size:
            exploding_bit_x = x+random.randrange(-1 * magnitude, magnitude)
            exploding_bit_y = y+random.randrange(-1 * magnitude, magnitude)
            
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,4)],(exploding_bit_x, exploding_bit_y),random.randrange(1,5))
            magnitude +=1
            pygame.display.update()
            clock.tick(100)
        explode = False
        
        
# Fire the tank shell
def fireShell(xy,tankx,tanky,turPos, gun_power, xlocation, barrier_width, randomHeight ):
    print "firing gun from x,y",xy
    fire = True
    
    startingShell = list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #print (startingShell[0], startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5 )
        
        startingShell[0] -= (12 - turPos)*2

        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015/(gun_power/50.0))**2) - (turPos+turPos/(12 - turPos)))

        if startingShell[1] > display_height - ground_height:
            #print("Last shell: ", startingShell[0], startingShell[1])
            # this may be incorrect - "display_height - ground_height" may need to be enclosed in ()
            hit_x = int((startingShell[0] * display_height - ground_height)/(startingShell[1]))
            hit_y = int(display_height - ground_height)
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x, hit_y)
            fire = False
            
        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation
        
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight
        
        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            #print("Last shell: ", startingShell[0], startingShell[1])
            hit_x = int(startingShell[0])
            hit_y = int(startingShell[1])
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x, hit_y)
            fire = False
            
        
        pygame.display.update()
        clock.tick(50)

# Fire the tank shell
def e_fireShell(xy,tankx,tanky,turPos, gun_power, xlocation, barrier_width, randomHeight, ptankx, ptanky ):
    
    
    currentPower = 1
    power_found = False
    
    while not power_found:
        currentPower +=1
        # cap the power level at 100
        if currentPower > 100:
            power_found = True

        fire = True
        startingShell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5 )
            
            startingShell[0] += (12 - turPos)*2
    
            startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015/(currentPower/50.0))**2) - (turPos+turPos/(12 - turPos)))
    
            if startingShell[1] > display_height - ground_height:
                # this may be incorrect - "display_height - ground_height" may need to be enclosed in ()
                hit_x = int((startingShell[0] * display_height - ground_height)/(startingShell[1]))
                hit_y = int(display_height - ground_height)
                #explosion(hit_x, hit_y)
                if ptankx+15 > hit_x > ptankx - 15:
                    print("Target acquired!")
                    power_found = True
                fire = False
                
            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation
            
            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height - randomHeight
            
            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int(startingShell[0])
                hit_y = int(startingShell[1])
                #explosion(hit_x, hit_y)
                fire = False
                    
    print("Starting the real fire!")
    fire = True
    startingShell = list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #print (startingShell[0], startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5 )
        
        startingShell[0] += (12 - turPos)*2

        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015/(currentPower/50.0))**2) - (turPos+turPos/(12 - turPos)))

        if startingShell[1] > display_height - ground_height:
            #print("Last shell: ", startingShell[0], startingShell[1])
            # this may be incorrect - "display_height - ground_height" may need to be enclosed in ()
            hit_x = int((startingShell[0] * display_height - ground_height)/(startingShell[1]))
            hit_y = int(display_height - ground_height)
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x, hit_y)
            fire = False
            
        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation
        
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight
        
        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell: ", startingShell[0], startingShell[1])
            hit_x = int(startingShell[0])
            hit_y = int(startingShell[1])
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x, hit_y)
            fire = False
            
        
        pygame.display.update()
        clock.tick(50)



def power(level):
    text = smallfont.render("Power: "+str(level)+"%", True, black)
    gameDisplay.blit(text, [display_width/2,0])


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
        message_to_screen("Welcome to Tanks",green,-100,"large")
        message_to_screen("The objective is to shoot and destroy",black,-30,"small")
        message_to_screen("the enemy tanks before they destroy you.",black,10,"small")
        message_to_screen("The more tanks you destroy, the harder they get.",black,50,"small")

        
        button("Play", 150,500, 100, 50, green, light_green, action = "play")
        button("Controls", 350,500, 100, 50, yellow, light_yellow, action = "controls")
        button("Quit", 550,500, 100, 50, red, light_red, action = "quit")
        
        pygame.display.update()
        clock.tick(15)

def health_bars(player_health, enemy_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
         player_health_color = red

    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
         enemy_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (680,25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color,  (20,25, enemy_health, 25))


# main game loop
def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15
    barrier_width = 50
    
    player_health = 100
    enemy_health = 100
    
    
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0
    
    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9
    
    fire_power = 50
    power_change = 0
    
    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.6)
    # define guns for the initial call
    gun = tank(mainTankX, mainTankY, currentTurPos)
    enemy_gun = enemy_tank(enemyTankX, enemyTankY, 7 )

    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over", red, -50, size = "large")
            message_to_screen("Press C to play again, or Q to quit", black, 50, size = "medium")
            pygame.display.update()
        
        while gameOver == True:
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
                    tankMove = -5
                    
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                
                elif event.key == pygame.K_UP:
                    changeTur = 1
                    
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE:
                    fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power, xlocation, barrier_width, randomHeight)
                    e_fireShell(enemy_gun,enemyTankX,enemyTankY,7,50, xlocation, barrier_width, randomHeight,mainTankX,mainTankY)
                    
                elif event.key == pygame.K_a:
                    power_change = -1
                
                elif event.key == pygame.K_d:
                    power_change = 1
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0
                    
        mainTankX += tankMove
        currentTurPos += changeTur
        # my version of out of bounds handling
        if currentTurPos < 0:
            currentTurPos = 0
        elif currentTurPos > 8:
            currentTurPos = 8
            
        if mainTankX - (tankWidth/2) < xlocation + barrier_width:
            mainTankX += 5
        
        
        gameDisplay.fill(white)
        health_bars(player_health, enemy_health)
        gun = tank(mainTankX, mainTankY, currentTurPos)
        # enemy elevation fixed at 7 for now
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 7 )

        fire_power += power_change
        
        # ensure we stay within 1-100
        if fire_power < 1:
            fire_power = 1
        elif fire_power > 100:
            fire_power = 100
            
        power(fire_power)
        
        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(green, rect = [0, display_height-ground_height, display_width, ground_height])
        
        pygame.display.update()
        clock.tick(FPS)
        
        
    
    # unitialize
    pygame.quit()
    
    quit()

game_intro()
gameLoop()


