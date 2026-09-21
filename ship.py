import pygame

from bullet import Bullet

class Ship:
    def __init__(self, screen, my_settings):
        self.screen = screen
        self.my_settings = my_settings
        self.image = pygame.image.load("images/spaseship.bmp")
        self.image.set_colorkey((0, 0, 128))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_right and self.rect.right <= self.my_settings.screen_width:
            self.rect.x += self.my_settings.ship_speed
        if self.moving_left and self.rect.x >= 0:
            self.rect.x -= self.my_settings.ship_speed
        if self.moving_top and self.rect.top >= 0:  # Adjusted boundary
            self.rect.y -= self.my_settings.ship_speed
        if self.moving_bottom and self.rect.bottom <= self.my_settings.screen_height:
            self.rect.y += self.my_settings.ship_speed

    def shoot(self, bullets):
        if self.my_settings.bullets_left > 0:
            bullet = Bullet(self.screen, self.my_settings, self)
            bullets.add(bullet)
            self.my_settings.bullets_left -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)