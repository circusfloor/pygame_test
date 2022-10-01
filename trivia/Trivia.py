import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('The Trivia Game')
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)
white = 255, 255, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0


def print_text(font, x, y, text, color=(255, 255, 255), shadow=True):
    if shadow:
        imgtext = font.render(text, True, (0, 0, 0))
        screen.blit(imgtext, (x-2, y-2))

    imgtext = font.render(text, True, color)
    screen.blit(imgtext, (x, y))


class Trivia:
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        # 读取问题数据
        with open(filename, 'r') as f:
            trivia_data = f.readlines()

            for i in trivia_data:
                self.data.append(i.strip())
                self.total += 1

    def show_question(self):
        print_text(font1, 210, 5, 'TRIVIA GAME')
        print_text(font2, 190, 500-20, 'Press Keys(1-4) To Answer', purple)

        self.correct = int(self.data[self.current + 5])

        question = self.current // 6 + 1
        print_text(font1, 5, 80, 'QUESTION' + str(question))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct-1] = green
            print_text(font1, 230, 380, 'CORRECT!', green)
            print_text(font2, 170, 420, 'Press Enter For Next Question', green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.wronganswer-1] = red
            self.colors[self.correct-1] = green
            print_text(font1, 230, 380, 'INCORRECT!', red)
            print_text(font2, 170, 420, 'Press Enter For Next Question', red)

        print_text(font1, 5, 170, 'ANSWERS')
        print_text(font2, 20, 210, '1-' + self.data[self.current + 1], self.colors[0])
        print_text(font2, 20, 240, '2-' + self.data[self.current + 2], self.colors[1])
        print_text(font2, 20, 270, '3-' + self.data[self.current + 3], self.colors[2])
        print_text(font2, 20, 300, '4-' + self.data[self.current + 4], self.colors[3])

    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0


trivia = Trivia('text.txt')

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

        trivia.show_question()

        pygame.display.update()
