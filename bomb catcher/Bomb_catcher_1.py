import pygame
import sys
import random
from pygame.locals import *

# 主函数
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Bomb Catcher')

# 属性
lives = 3
game_over = True
score = 0
pos_x = random.randint(25, 1175)
pos_y = -50
vel_x = 5
vel_y = 0.2
color = random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)
font = pygame.font.Font(None, 40)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        # if event.type == MOUSEMOTION:
        #     mouse_x, mouse_y = event.pos
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_over:
                    game_over = False
                    score = 0
                    lives = 3

    mouse_x, mouse_y = pygame.mouse.get_pos()
    b1, b2, b3 = pygame.mouse.get_pressed()
    screen.fill((0, 0, 0))

    if not game_over:
        pos_y += vel_y
        circle = pygame.draw.circle(screen, color, (pos_x, pos_y), 50, 0)

    if pos_x - 25 < mouse_x < pos_x + 25 and pos_y - 25 < mouse_y < pos_y + 25:
        if b1 or b2 or b3:
            color = random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)
            pos_y = -50
            pos_x = random.randint(25, 1175)
            score += 1

    if lives == 0:
        game_over = True
        font3 = pygame.font.Font(None, 80)
        font3 = font3.render('Press enter start game', True, (200, 200, 0))
        screen_rect = screen.get_rect()
        screen.blit(font3, (screen_rect.left + 100, screen_rect.centery))

    if pos_y > 800:
        pos_y = -50
        pos_x = random.randint(25, 1175)
        lives -= 1

    font1 = font.render('Score: ' + str(score), True, (200, 200, 0))
    screen.blit(font1, (900, 50))
    font2 = font.render('Lives: ' + str(lives), True, (200, 200, 0))
    screen.blit(font2, (900, 75))
    pygame.display.update()
