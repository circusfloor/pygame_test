import pygame, sys, math, random
from pygame.locals import *


def wrap_angle(angle):
    return angle % 360


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgtext = font.render(text, True, color)
    screen.blit(imgtext, (x, y))


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def setx(self, x):
        self._x = x

    x = property(getx, setx)

    def gety(self):
        return self._y

    def sety(self, y):
        self._y = y

    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f".format(self._x) +\
            ",Y:" + ":.0f".format(self._y) + "}"


# 游戏初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Orbit')
font = pygame.font.Font(None, 18)

# 读取位图
space = pygame.image.load('space.png').convert()
planet = pygame.image.load('planet2.png').convert_alpha()
ship = pygame.image.load('freelance.png').convert_alpha()
width, height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width//2, height//2))

radius = 250
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.blit(space, (0, 0))

    width, height = planet.get_size()
    screen.blit(planet, (400 - width / 2, 300 - height / 2))

    angle = wrap_angle(angle - 0.1)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.x = math.cos(math.radians(angle)) * radius
    width, height = ship.get_size()
    screen.blit(ship, (400+pos.x-width//2, 300+pos.y-height//2))

    pygame.display.update()
