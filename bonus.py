import pygame
from pygame.sprite import Sprite
from random import randint

class Bonus(Sprite):
    def __init__(self, screen, my_settings):
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings
        self.image = pygame.image.load('images/bonus.png')  # Replace with your bonus image
        self.image.set_colorkey((0, 0, 128))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, my_settings.screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 3  # Slower fall speed than meteorites
        if self.rect.top > self.my_settings.screen_height:
            self.kill()  # Remove bonus when it leaves the screen

    def blitme(self):
        self.screen.blit(self.image, self.rect)