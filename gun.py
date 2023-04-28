import pygame
from pygame.sprite import Sprite

class Gun(Sprite):
    def __init__(self,screen): #инициализация главного героя
        super(Gun, self).__init__()
        self.screen = screen #получение экрана
        self.image = pygame.image.load('images/cat.png')
        self.rect = self.image.get_rect() #получение картинки как прямоугольный объект
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx) #преобразование числа в вещественное
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self): #отрисовка изображения
        self.screen.blit(self.image, self.rect)

    def update_gun(self): #обновление позиции г.г.
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5
        self.rect.centerx = self.center

    def create_gun(self): #размещает пушку по центру внизу
        self.center = self.screen_rect.centerx

