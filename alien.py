import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ a class to represecnt single alien in the fleet """

    def __init__(self,ai_settings,screen):
        """ initialize the alien and set its starting position """
        super().__init__()
        self.screen = screen
    #assing the value by ai_settings so that we have the access to the ships speed
        self.ai_settings = ai_settings
    #loads the alien image and set its rectangle
        self.image = pygame.image.load('images/alien.bmp')
        self.rect  = self.image.get_rect()
    # start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    #storing the decimal value for ships center
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moves the alien towards the right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """returns True if your alien reches the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
