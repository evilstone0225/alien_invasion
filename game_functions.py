import sys
import pygame
from bullet import Bullet
from time import sleep
from alien import Alien

def check_events(ai_settings,screen,ship,bullets):
    """ respond to mouse click and keypress events """
    #watch for the keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydowm_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move the ship to the right
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()



def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """updated images on the screen and flips the images"""
    screen.fill(ai_settings.bg_color)
    #redraw all the bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # used to draw the image to the screen specidfied by the get_rect()
    ship.blitme()
    #to display the alien
    #alien.blitme()

    aliens.draw(screen)
    #Make the screen (visible)available on the display untill the user interrupts
    pygame.display.flip()


def update_bullets(ai_settings,screen,ship,aliens,bullets):
    """ a function to update the bullets and remov them as they reach 0 position"""
    bullets.update()
    # to get rid of the extra bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets)

def check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets):
    
    """check for any update occur in the bullet is yes then,
    it checks for the collision"""
    collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
    #print(len(bullets))
    if len(aliens) == 0:
        """Destroy the bullets and create the new fleet of alien"""
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
   


def fire_bullet(ai_settings,screen,ship,bullets):
    """ Firing a ullets if limit not reached """
    #a condition to allow only few bullets at a time on the screen
    if len(bullets) <= ai_settings.bullet_allowed:
        #create a new bullet and add it to the bullet group()
        new_bullets = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullets)


def create_fleet(ai_settings,screen,ship,aliens):
    """create a fleet of aliens """
    #create an alien to find the number of rows
    #spacing between each alien is equal to the one aliens width in the screen
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_of_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #create the fleet of aliens
    for number_of_row in range(number_of_rows):         
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,number_of_row)


def get_number_alien_x(ai_settings, alien_width):
    """ Determines the number of alien that fit in the row """
    alien_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(alien_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,number_of_rows):
    """areate an alien and fits it in the row"""
    #create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_of_rows
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """ determines the number of rows that can fit in the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_of_rows = int(available_space_y / (2 * ship_height))
    return number_of_rows

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """ check wheter fleet is at the end ....if yes than change all the fleets position"""
    """updates the position of all the alien """    
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
        print("OOP's...SHIP HIT!!!")
        check_alien_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def check_fleet_edges(ai_settings, aliens): 
    """Respond appropriately if any aliens have reached an edge."""      
    for alien in aliens.sprites():        
        if alien.check_edges():   
            change_fleet_direction(ai_settings, aliens)   
            break 

def change_fleet_direction(ai_settings,aliens):
    """change the diretion of the fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """It will repond to the ship being hit by the alien"""
    if stats.ship_left > 0:
        #decrement the ship value from left_ship
        stats.ship_left -= 1

        #empty the alien and the bullets
        aliens.empty()
        bullets.empty()

        #create the new fkleet and refactor the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship() 

        #Pause 
        sleep(0.5)
    else:
        stats.game_active = False

def check_alien_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """check whether the alien reaches the bottom or not"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        #checking that it has reached the bottom or not     
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break    
