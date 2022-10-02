import pygame, sys, random, time
from pygame.locals import *


def print_text(font, x, y, text, color=(0, 0, 0)):
    imgtext= font.render(text, True, color)
    screen.blit(imgtext, (x, y))


# 主函数
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Typing Speed')

# 属性
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
white = 255, 255, 255
yellow = 200, 200, 0
key_flag = False
correct_answer = 97  # a
game_over = True
score = 0
current = 0
clock_start = 0
seconds = 11

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type == KEYUP:
            key_flag = False

        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            if game_over:
                game_over = False
                score = 0
                seconds = 11

                clock_start = time.perf_counter()

    current = time.perf_counter() - clock_start
    print(time.perf_counter(), clock_start)
    speed = score * 6

    if seconds - current < 0:
        game_over = True
    elif current <= 10:
        if keys[correct_answer]:
            correct_answer = random.randint(97, 122)
            score += 1

    screen.fill((255, 255, 255))

    print_text(font1, 800, 50, 'Score:' + str(score))
    print_text(font1, 50, 100, 'Speed:' + str(speed) + 'letters/min')
    if game_over:
        print_text(font1, 50, 160, 'Press Enter to start...')
    if not game_over:
        print_text(font1, 50, 80, 'Time: ' + str(int(seconds - current)))
    # print(seconds, current, seconds - current)
    print_text(font2, 50, 240, chr(correct_answer-32), yellow)

    pygame.display.update()


