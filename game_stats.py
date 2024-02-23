class GameStats:
    """Track statistics for the Alien Invasion game"""

    def __init__(self, ai_game):
        """Initialize game statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
        self.high_score = 0

        # Start the game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initizalize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1