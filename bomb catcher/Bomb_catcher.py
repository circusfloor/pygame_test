import pygame, sys, random
from pygame.locals import *


# 主函数
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Bomb Catcher')

# 属性
lives = 3
game_over = True
score = 0
x = random.randint(0, 1200)
y = -50
vel_x = 5
vel_y = 5
color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            print('1')
        elif event.type == KEYUP:
            print('2')

        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            if game_over:
                game_over = False
                score = 0

    y += vel_y
    pygame.draw.circle(screen, color, (x, y), 50, 5)

    pygame.display.update()


