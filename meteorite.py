import pygame
from pygame.sprite import Sprite


class Meteorite(Sprite):
    def __init__(self, screen, my_settings, vers_image=0):
        super(Meteorite, self).__init__()
        self.screen = screen
        self.my_settings = my_settings
        if vers_image == 0:
            self.image = pygame.image.load('images/астероид.png')
        elif vers_image == 1:
            self.image = pygame.image.load('images/meteorite.bmp')
        else:
            self.image = pygame.image.load('images/asteroid.bmp')
        self.image.set_colorkey((0, 0, 128))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def update(self):
        self.rect.y += self.my_settings.meteorite_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
