import pygame
# Slither, Pygame Tutorial #04

x = pygame.init()

print(x)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

# update the entire surface
pygame.display.flip()

# update part of the surface (optionally) or the entire surface (default)
pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
#        print(event)
        if event.type == pygame.QUIT:
            print 'Quit event detected, quitting game'
            gameExit = True
            

    


# unitialize
pygame.quit()

quit()

