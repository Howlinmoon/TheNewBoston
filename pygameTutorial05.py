import pygame

pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0.255)
black = (255,255,255)


gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

# update the entire surface
pygame.display.flip()


gameExit = False

while not gameExit:
    for event in pygame.event.get():
#        print(event)
        if event.type == pygame.QUIT:
            print 'Quit event detected, quitting game'
            gameExit = True
            
    gameDisplay.fill(white)
    pygame.display.update()
    
    
    

# unitialize
pygame.quit()

quit()

