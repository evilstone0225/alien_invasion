import pygame

class Ship():
# it takes two parameters self and the other screen where we are going to displ the image
    def __init__(self,ai_settings,screen):
        """ initialize the ship and set it's initial position """
        self.screen = screen

    #loads the image
        self.image = pygame.image.load('images/ship.bmp')
    # to ge access to the surface attribute of rect
        self.rect  = self.image.get_rect()
    #storing screen's rect to the screen_rect
        self.screen_rect = screen.get_rect()
    #assing the value by ai_settings so that we have the access to the ships speed
        self.ai_settings = ai_settings
     # Start each new ship at the bottom center of the screen. x
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    #storing the decimal value for ships center
        self.center = float(self.rect.centerx)

        #declaring a flag to check keypress
        self.moving_right = False
        self.moving_left = False



    def update(self):
        """ updates the postion of the moving flag to the right basedon the flag"""
        #updating thecenter value of the ship and not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #update the rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """display te ship in the center"""
        self.center = self.screen_rect.centerx