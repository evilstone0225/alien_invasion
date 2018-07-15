class Settings():
    """ A class to store all the setting of alien Invasion """
    def __init__(self):
    #SCREEN SETTINGS
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed_factor = 2.5
        self.ship_limit = 2

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
       # 1 indicates the movement in the right n -1 in the left 
        self.fleet_direction = 1

    #BULLET Settings
        self.bullet_color = (60,60,60)
        self.bullet_height = 20
        self.bullet_width = 10
        self.bullet_speed_factor = 3
        self.bullet_allowed = 4
