import pygame

class Ino(pygame.sprite.Sprite):
    #класс одного пришельца
 def __init__(self,screen): #инициализация и задание начальной позиции
    super(Ino, self).__init__() #тк дочерний класс, родительский - sprite
    self.screen = screen
    self.image = pygame.image.load('images/ino.png')
    self.rect = self.image.get_rect()
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)

 def draw(self): #вывод противника на экран
    self.screen.blit(self.image, self.rect) #метод блит позволяет отрисовывать объект на экран

 def update(self): #перемещение пришельцев
     self.y += 0.1
     self.rect.y = self.y

