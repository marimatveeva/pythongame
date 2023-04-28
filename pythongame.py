import pygame
import sys
from gun import Gun
from ino import Ino

def run():
    pygame.init() #инициализация игры
    screen = pygame.display.set_mode((1200, 800)) #создание экрана и его размера
    pygame.display.set_caption("Sleepy Fight")
    bg_color = (0, 0, 0) #создание цвета экрана
    gun = Gun(screen)

    while True:
        for event in pygame.event.get(): #обработка действий пользователя
           if event.type == pygame.QUIT: #закрытие экрана
               sys.exit()

        screen.fill(bg_color)#цвет фона
        gun.output()
        pygame.display.flip()#прорисовка последнего экрана

run()

