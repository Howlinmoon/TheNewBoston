import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# PyGame Tutorial #92

verticies = (
    (1, -1, -1),         
    (1, 1, -1),         
    (-1, 1, -1),         
    (-1, -1, -1),         
    (1, -1, 1),         
    (1, 1, 1),         
    (-1, -1, 1),         
    (-1, 1, 1)         
 )

edge = (
    (0,1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

