import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ class which is inherites the features of the sprite class """

    def __init__(self,ai_settings,screen,ship):

        """ creating the bullet obj at ships current position """
        super().__init__()
        self.screen = screen

     #need to creat the bullet rect at (0,0) position then setting it to correct one
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

         #storing the bullets position at decimal vallue
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed_factor

    def update(self):
        """ update the bullet position """
        #moving the bullet upwards in direction
        self.y -= self.speed
        #update the rect posotion
        self.rect.y = self.y

    def draw_bullet(self):
        """ fun. to draw the bullets on the screen """
        pygame.draw.rect(self.screen,self.color,self.rect)
