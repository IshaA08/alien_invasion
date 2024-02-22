class GameStats:
    """Track statistics for the Alien Invasion game"""

    def __init__(self, ai_game):
        """Initialize game statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initizalize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit