import pygame
from pygame.sprite import Sprite
from meteorite import Meteorite
from bonus import Bonus
from random import randint

pygame.init()
images = pygame.image.load('images/fon.jpg')
rect = images.get_rect()
font = pygame.font.SysFont("comicsansms", 25)

def update_screen(screen, my_settings, ship, meteorites, bullets, bonuses):
    global images, rect, font
    image = pygame.transform.scale(images, screen.get_size())
    screen_rect = screen.get_rect()
    my_settings.screen_width, my_settings.screen_height = screen.get_size()
    screen.blit(image, rect)
    ship.update()
    ship.blitme()
    make_meteorite(screen, my_settings, meteorites)
    del_meteorite(my_settings, meteorites)
    make_bonus(screen, my_settings, bonuses)
    
    # Update and draw bullets
    bullets.update()
    bullets.draw(screen)
    
    # Update and draw meteorites
    for meteorite in meteorites:
        meteorite.update()
    meteorites.draw(screen)
    
    # Update and draw bonuses
    bonuses.update()
    bonuses.draw(screen)
    
    # Collisions
    if pygame.sprite.spritecollideany(ship, meteorites):
        my_settings.aktive = False
    if pygame.sprite.spritecollide(ship, bonuses, True):  # Collect bonus
        my_settings.points += my_settings.bonus_points
        my_settings.bullets_left = my_settings.max_bullets
    
    # Bullet-meteorite collisions
    pygame.sprite.groupcollide(bullets, meteorites, True, True)
    
    # Display points and bullets
    value = font.render(f"Score: {my_settings.points}  Bullets: {my_settings.bullets_left}", True, 'yellow')
    screen.blit(value, [0, 0])
    pygame.display.flip()

def check_event(ship, my_settings, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            my_settings.aktive = False
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, my_settings, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship, my_settings, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_top = True
    if event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    if event.key == pygame.K_SPACE:  # Shoot with spacebar
        ship.shoot(bullets)
    if event.key == pygame.K_q:
        my_settings.aktive = False

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_top = False
    if event.key == pygame.K_DOWN:
        ship.moving_bottom = False

def make_meteorite(screen, my_settings, meteorites):
    if len(meteorites) < my_settings.max_meteorites:
        numb = randint(1, 4)
        if numb == 3:
            new_meteorite = Meteorite(screen, my_settings, 1)
        elif numb == 4:
            new_meteorite = Meteorite(screen, my_settings, 2)
        else:
            new_meteorite = Meteorite(screen, my_settings, 0)
        x = randint(1, my_settings.screen_width)
        y = randint(-500, -25)
        new_meteorite.rect.x = x
        new_meteorite.rect.y = y
        if not pygame.sprite.spritecollideany(new_meteorite, meteorites):
            meteorites.add(new_meteorite)

def del_meteorite(my_settings, meteorites):
    for meteorite in meteorites:
        if meteorite.rect.y >= my_settings.screen_height:
            meteorites.remove(meteorite)
            my_settings.points += 1

def make_bonus(screen, my_settings, bonuses):
    if not bonuses and randint(1, my_settings.bonus_spawn_chance) == 1:
        new_bonus = Bonus(screen, my_settings)
        bonuses.add(new_bonus)