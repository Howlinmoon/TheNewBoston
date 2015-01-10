import pygame
import random

# Pygame Tutorial #85

pygame.init()

display_width = 640
display_height = 480

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



# main game loop
def gameLoop():
    FPS = 30
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print 'Quit event detected, quitting game'
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                    
                elif event.key == pygame.K_RIGHT:
                    pass
                
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pass
                    
        
        gameDisplay.fill(green)
        clock.tick(FPS)
        
        
    
    # unitialize
    pygame.quit()
    quit()

gameLoop()


