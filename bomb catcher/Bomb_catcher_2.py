import pygame
import sys
import random
from pygame.locals import *


class Settings:
    """游戏属性"""

    def __init__(self):
        # 基础设置
        self.lives = 3
        self.score = 0
        self.level = 1
        self.color = 200, 200, 200
        self.font1 = pygame.font.Font(None, 40)
        self.font2 = pygame.font.Font(None, 40)
        self.vel_y = 0.3

        # 游戏状态
        self.game_over = True


class Circle:
    """创造球的类"""

    def __init__(self, screen):
        """球的属性"""
        self.pos_x = random.randint(25, 1175)
        self.pos_y = -50
        self.color = random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)
        self.screen = screen
        self.total = 0

    def update(self, settings):
        """更新球的位置，向下落"""
        self.pos_y += settings.vel_y

    def draw_circle(self):
        """绘制球"""
        pygame.draw.circle(self.screen, circle.color, (self.pos_x, self.pos_y), 50, 0)


class Basket:
    """创建篮筐的类"""

    def __init__(self, screen):
        """篮筐属性"""
        self.screen = screen

        # 基本属性
        self.width = 200
        self.height = 30
        self.color = 100, 100, 100
        self.speed = 1.5

        # 篮筐的大小和位置
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.bottom - 30

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新篮筐的位置"""
        if self.moving_right:
            self.rect.move_ip(self.speed, 0)
        if self.moving_left:
            self.rect.move_ip(-self.speed, 0)

    def draw_basket(self):
        """绘制篮筐"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Function:

    def get_mouse_pos(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        screen.fill((0, 0, 0))
        return mouse_x, mouse_y, b1

    def event_check(self, settings, circle, basket):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if settings.game_over:
                        settings.game_over = False
                        settings.score = 0
                        settings.lives = 3
                        circle.total = 0
                        settings.level = 1
                        settings.vel_y = 0.3
                if event.key == pygame.K_LEFT:
                    basket.moving_left = True
                if event.key == pygame.K_RIGHT:
                    basket.moving_right = True
            elif event.type == KEYUP:
                if event.key == pygame.K_RIGHT:
                    basket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    basket.moving_left = False

    def kill_circle(self, settings, circle, basket):
        mouse_x, mouse_y, b1 = self.get_mouse_pos()
        if circle.pos_x - 25 < mouse_x < circle.pos_x + 25 and \
                circle.pos_y - 25 < mouse_y < circle.pos_y + 25:
            if b1:
                circle.color = random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)
                circle.pos_y = -50
                circle.pos_x = random.randint(25, 1175)
                settings.score += 1
                circle.total += 1
        if basket.rect.x < circle.pos_x < basket.rect.x + 200 and circle.pos_y > 760:
            circle.color = random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)
            circle.pos_y = -50
            circle.pos_x = random.randint(25, 1175)
            settings.score += 1
            circle.total += 1

    def print_text(self, screen, settings):
        text1 = settings.font1.render('Score: ' + str(settings.score), True, (255, 128, 0))
        screen.blit(text1, (1000, 50))
        text2 = settings.font1.render('Lives: ' + str(settings.lives), True, (255, 128, 0))
        screen.blit(text2, (1000, 75))
        text2 = settings.font1.render('Level: ' + str(settings.level), True, (255, 128, 0))
        screen.blit(text2, (1000, 25))
        if settings.lives == 0:
            text3 = pygame.font.Font(None, 80)
            text3 = text3.render('Press Enter Restart', True, (255, 128, 0))
            screen_rect = screen.get_rect()
            screen.blit(text3, (screen_rect.left + 100, screen_rect.centery))

    def game_over_check(self, settings, circle):
        if settings.lives == 0:
            settings.game_over = True
            circle.total = 0
        if circle.pos_y > 800:
            circle.pos_y = -50
            circle.pos_x = random.randint(25, 1175)
            settings.lives -= 1

    def update_level(self, circle, settings):
        if circle.total >= 5:
            settings.level = 1 + circle.total // 5
            settings.vel_y = 0.3 + settings.level * 0.1

    def screen_update(self, screen, circle, settings, basket):
        screen.fill(settings.color)
        if not settings.game_over:
            circle.update(settings)
            circle.draw_circle()
        basket.update()
        basket.draw_basket()

        self.print_text(screen, settings)
        self.update_level(circle, settings)
        pygame.display.update()


# 主函数
pygame.init()
screen = pygame.display.set_mode((1200, 800))
settings = Settings()
circle = Circle(screen)
basket = Basket(screen)
pygame.display.set_caption('Bomb Catcher')

while True:
    Function().event_check(settings, circle, basket)
    Function().kill_circle(settings, circle, basket)
    Function().game_over_check(settings, circle)
    Function().screen_update(screen, circle, settings, basket)
