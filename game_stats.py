class GameStats():
    """ Track the statistics for the alien"""
    def __init__(self,ai_settings):
        """Initializt the stats"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset()
    def reset(self):
        """ Initialize the stats that we can change during the game"""
        self.ship_left = self.ai_settings.ship_limit
    