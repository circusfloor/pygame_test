import pygame, sys
from pygame.locals import *
from random import randint


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Drawing Lines')


while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 0))

    # 绘制线条
    for i in range(200):
        start_pos = (randint(0, 600), randint(0, 500))
        end_pos = (randint(0, 600), randint(0, 500))
        color = randint(0, 255), randint(0, 255), randint(0, 255)
        width = randint(2, 5)
        pygame.draw.line(screen, color, start_pos, end_pos, width)
        pygame.display.update()
