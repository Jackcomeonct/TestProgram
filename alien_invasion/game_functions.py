import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    if event.key == pygame.K_LEFT:
        ship.moveing_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    if event.key == pygame.K_LEFT:
        ship.moveing_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人并计算一行可容纳多少个外星人
    #外星人间距为外星人本身的宽度
    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number,row_number)

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - (3*alien_height)-ship_height
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def update_aliens(aliens):
    '''更新外星人群中所有的外星人位置'''
    aliens.update()

