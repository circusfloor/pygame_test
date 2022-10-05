import pygame, sys, math, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Orbit')

space= pygame.image.load('space.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.blit(space, (0, 0))

    pygame.display.update()
