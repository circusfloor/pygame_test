import pygame, sys
from pygame.locals import *
import math

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Drawing Arcs')

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((255, 255, 255))

    # 绘制弧形
    color = 100, 255, 200
    position = 200, 150, 200, 200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    pygame.display.update()
