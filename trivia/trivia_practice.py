import pygame
import sys
from pygame.locals import *


class Settings:
    def __init__(self):
        self.font1 = pygame.font.Font(None, 30)
        self.font2 = pygame.font.Font(None, 60)
        self.x = 100
        self.y = 100


class Trivia:
    def __init__(self, filename, screen):
        self.screen = screen

        # 问题属性
        self.data = []
        self.score = 0
        self.current = 0
        self.correct = 0
        self.scored = False
        self.failed = False

        # 读取问题文档
        with open(filename, 'r') as f:
            datas = f.readlines()
            for i in datas:
                self.data.append(i)

        self.total = len(self.data)

    def print_text(self, font, x, y, text, color=(255, 255, 255)):
        text_ = font.render(text, True, color)
        self.screen.blit(text_, (x, y))

    def next_question(self):
        if self.scored or self.failed:
            self.correct = 0
            self.scored = False
            self.failed = False
            self.current += 6
            if self.current >= self.total:
                self.current = 0

    def handle_input(self, number):
        if number == self.correct:
            self.scored = True
            self.score += 1
        else:
            self.failed = True

    def show_question(self, settings):
        self.correct = int(self.data[self.current + 5])

        if self.scored:
            self.print_text(settings.font2, 600, 700, 'CORRECT！', (0, 255, 0))
        elif self.failed:
            self.print_text(settings.font2, 600, 700, 'INCORRECT！', (255, 0, 0))

        self.print_text(settings.font2, settings.x, settings.y, self.data[self.current].strip())
        self.print_text(settings.font1, settings.x, settings.y + 60 + 1 * 30,
                        '1-' + self.data[self.current + 1].strip())
        self.print_text(settings.font1, settings.x, settings.y + 60 + 2 * 30,
                        '2-' + self.data[self.current + 2].strip())
        self.print_text(settings.font1, settings.x, settings.y + 60 + 3 * 30,
                        '3-' + self.data[self.current + 3].strip())
        self.print_text(settings.font1, settings.x, settings.y + 60 + 4 * 30,
                        '4-' + self.data[self.current + 4].strip())


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('TRIVIA GAME')

    settings = Settings()
    trivia = Trivia('text.txt', screen)

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_1:
                    trivia.handle_input(1)
                elif event.key == pygame.K_2:
                    trivia.handle_input(2)
                elif event.key == pygame.K_3:
                    trivia.handle_input(3)
                elif event.key == pygame.K_4:
                    trivia.handle_input(4)
                elif event.key == pygame.K_RETURN:
                    trivia.next_question()

        screen.fill((0, 0, 0))
        trivia.show_question(settings)

        pygame.display.update()


run_game()
