import pygame
import sys
from pygame.locals import *
from random import randint


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Drawing Rectangles')
pos_x = 300
pos_y = 250
vel_x = 0.2
vel_y = 0.1
color = 255, 255, 0

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    # 移动矩形
    pos_x += vel_x
    pos_y += vel_y

    # 保持矩形在屏幕上
    if pos_x > 500 or pos_x < 0:
        color = randint(0, 255), randint(0, 255), randint(0, 255)
        vel_x = - vel_x
    if pos_y > 400 or pos_y < 0:
        color = randint(0, 255), randint(0, 255), randint(0, 255)
        vel_y = - vel_y

    # 绘制矩形
    width = 0
    pos = pos_x, pos_y, 100, 100
    pygame.draw.rect(screen, color, pos, width)

    pygame.display.update()
    