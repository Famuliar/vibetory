import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, my_settings, ship):
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings
        self.image = pygame.Surface((5, 15))  # Simple bullet shape
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def update(self):
        self.rect.y -= self.my_settings.bullet_speed
        if self.rect.bottom < 0:
            self.kill()  # Remove bullet when it leaves the screen

    def blitme(self):
        self.screen.blit(self.image, self.rect)