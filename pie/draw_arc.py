import pygame, sys
from pygame.locals import *
import math
from random import randint


pygame.init()
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((1920, 1080), flags)
pygame.display.set_caption('Drawing Arcs')
pos_x = 300
pos_y = 150

vel_x = 5
vel_y = 5


while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((255, 255, 255))

    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 600 or pos_x < 0:
        vel_x = - vel_x
    if pos_y > 500 or pos_y < 0:
        vel_y = - vel_y

    # 绘制弧形
    for i in range(100):
        color = randint(0, 255), randint(0, 255), randint(0, 255)
        position = pos_x, pos_y, 200, 200
        start_angle = math.radians(0)
        end_angle = math.radians(180)
        width = 8
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

        pygame.display.update()
