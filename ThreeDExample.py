import pygame
import random

# Pygame Tutorial #89

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)
red = (200,0,0)
light_red = (255,0,0)

green = (34,177,76)
light_green = (0,255,0)

blue = (0,0.255)
black = (0,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('3D Tutorial')

# Drawing a 2.5d cube
def cube(startPoint, fullsize):
    # upper left corner
    node_1 =[startPoint[0], startPoint[1]]
    # upper right corner
    node_2 =[startPoint[0]+fullsize, startPoint[1]]
    # bottom left corner
    node_3 =[startPoint[0], startPoint[1]+fullsize]
    # bottom right corner
    node_4 =[startPoint[0]+fullsize, startPoint[1]+fullsize]
    
    offset = int(fullsize / 2)
   
    x_mid = int(display_width / 2)
    x_offset = -1 * int(startPoint[0] - x_mid)
    if x_offset > 100:
        x_offset = 100
    elif x_offset < -100:
        x_offset = -100
    # second square, upper left corner 
    node_5 = [node_1[0]+x_offset, node_1[1]-offset]
    # second square, upper right corner
    node_6 = [node_2[0]+x_offset, node_2[1]-offset]
    # second square, bottom left corner
    node_7 = [node_3[0]+x_offset, node_3[1]-offset]
    # second square, bottom right corner
    node_8 = [node_4[0]+x_offset, node_4[1]-offset]

    # first square
    # top line
    pygame.draw.line(gameDisplay, white, (node_1), (node_2))
    # bottom line
    pygame.draw.line(gameDisplay, white, (node_3), (node_4))
    # left line
    pygame.draw.line(gameDisplay, white, (node_1), (node_3))
    # right line
    pygame.draw.line(gameDisplay, white, (node_2), (node_4))

    pygame.draw.circle(gameDisplay, light_green, node_1, 5)
    pygame.draw.circle(gameDisplay, light_green, node_2, 5)
    pygame.draw.circle(gameDisplay, light_green, node_3, 5)
    pygame.draw.circle(gameDisplay, light_green, node_4, 5)
    
    # second square
    # top line
    pygame.draw.line(gameDisplay, white, (node_5), (node_6))
    # bottom line
    pygame.draw.line(gameDisplay, white, (node_7), (node_8))
    # left line
    pygame.draw.line(gameDisplay, white, (node_5), (node_7))
    # right line
    pygame.draw.line(gameDisplay, white, (node_6), (node_8))
    
    pygame.draw.circle(gameDisplay, light_green, node_5, 5)
    pygame.draw.circle(gameDisplay, light_green, node_6, 5)
    pygame.draw.circle(gameDisplay, light_green, node_7, 5)
    pygame.draw.circle(gameDisplay, light_green, node_8, 5)


    # connect the squares
    pygame.draw.line(gameDisplay, white, (node_1), (node_5))
    pygame.draw.line(gameDisplay, white, (node_2), (node_6))
    pygame.draw.line(gameDisplay, white, (node_3), (node_7))
    pygame.draw.line(gameDisplay, white, (node_4), (node_8))



# main game loop
def gameLoop():
    location = [300,200]
    size = 200
    current_move = 0
    
    z_move = 0
    z_location = 11
    
    y_move = 0
    
    FPS = 30
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print 'Quit event detected, quitting game'
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_move = -5
                    
                elif event.key == pygame.K_RIGHT:
                    current_move = 5

                elif event.key == pygame.K_UP:
                    y_move = -5
                    current_move = -1
                    
                elif event.key == pygame.K_DOWN:
                    y_move = 5
                    current_move = +1
                    
                elif event.key == pygame.K_a:
                    size -= 10
                    if size < 0:
                        size = 10
                    
                elif event.key == pygame.K_d:
                    size += 10
                    if size > 200:
                        size = 200

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    current_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
                    current_move = 0
                    
        
        gameDisplay.fill(black)
        z_location += z_move
        if z_location > 200:
            z_location = 0


        current_size = int(size / (z_location * 0.1))
        location[0] += current_move
        location[1] += y_move
        cube(location, current_size)
        pygame.display.update()
        clock.tick(FPS)
        
        
    
    # unitialize
    pygame.quit()
    quit()

gameLoop()


