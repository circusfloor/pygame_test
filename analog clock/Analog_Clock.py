import pygame
import sys
import random
import math
from datetime import datetime
from pygame.locals import *


def print_text(font, x_, y_, text, color_=(255, 255, 255)):
    imgtext = font.render(text, True, color_)
    screen.blit(imgtext, (x_, y_))


def wrap_angle(angle_):
    return angle_ % 360


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Analog Clock')


pos_x = 300
pos_y = 250
radius = 200
angle = 360
font1 = pygame.font.Font(None, 36)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0, 0, 100))

    # 绘制圆
    angle += 1
    if angle >= 360:
        angle = 0
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = r, g, b

    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius

    pos = (int(pos_x + x), int(pos_y + y))
    pygame.draw.circle(screen, color, pos, 10, 0)

    # 绘制1_12数字
    for n in range(1, 13):
        angle_n = math.radians(n * (360/12) - 90)
        x = math.cos(angle_n) * (radius-20) - 10
        y = math.sin(angle_n) * (radius-20) - 10
        print_text(font1, pos_x+x, pos_y+y, str(n))

    # 获取当前时间
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    # 绘制时针
    hour_angle = wrap_angle(hours * (360/12) - 90)
    hour_angle = math.radians(hour_angle)
    hour_x = math.cos(hour_angle) * (radius-80)
    hour_y = math.sin(hour_angle) * (radius-80)
    target = (pos_x+hour_x, pos_y+hour_y)
    pygame.draw.line(screen, color, (pos_x, pos_y), target, 25)

    # 绘制分针
    min_angle = wrap_angle(minutes * (360/12) - 90)
    min_angle = math.radians(min_angle)
    min_x = math.cos(min_angle) * (radius-60)
    min_y = math.sin(min_angle) * (radius-60)
    target = (pos_x+min_x, pos_y+min_y)
    pygame.draw.line(screen, color, (pos_x, pos_y), target, 12)

    # 绘制秒针
    sec_angle = wrap_angle(minutes * (360/12) - 90)
    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius-40)
    sec_y = math.sin(sec_angle) * (radius-40)
    target = (pos_x+sec_x, pos_y+sec_y)
    pygame.draw.line(screen, color, (pos_x, pos_y), target, 6)

    pygame.draw.circle(screen, color, (pos_x, pos_y), 10)
    print_text(font1, 10, 0, str(hours) + ':' + str(minutes) + ':' + str(seconds))

    pygame.display.update()
