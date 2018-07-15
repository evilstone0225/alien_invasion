import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():

    #initialize the game and create the screen oject
    pygame.init()
    #creatng the instance of Settings()
    ai_settings = Settings()
    
    #creating the instanc of the gamestaticss
    stats = GameStats(ai_settings)

    #passing the imported data into the set_mode
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    #adds caption to our screen
    pygame.display.set_caption("_Alien Invasion_")

    #make a ship by passing the screen attribute in it
    ship = Ship(ai_settings,screen)

    #make a group to store the bullet
    bullets = Group()
    #group of aliens
    aliens = Group()

    #make the instance of the alien
    alien = Alien(ai_settings,screen)
    #creating te fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #start the main loop for the game
    while True:
        #call the fun. that checks the interrupt event
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        #to fill the bg with diff. color
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()
