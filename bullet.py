import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun): #создание пули в текущей позиции гг
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 20, 12)
        self.color = 139,195,74
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update (self):
        self.y -= self.speed #координата y уменьшается на заданную скорость
        self.rect.y = self.y #обновление позиции пули

    def draw_bullet(self): #отрисовка пули на экране
        pygame.draw.rect(self.screen, self.color, self.rect )




