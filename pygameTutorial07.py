import pygame

pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0.255)
black = (0,0,0)


gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

# update the entire surface
pygame.display.flip()


gameExit = False

lead_x = 300
lead_y = 300



while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print 'Quit event detected, quitting game'
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            elif event.key == pygame.K_RIGHT:
                lead_x += 10
                
            
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])

    
    pygame.display.update()
    
    
    

# unitialize
pygame.quit()

quit()


