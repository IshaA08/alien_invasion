class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (207, 220, 227)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.score_scale = 1.3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullets_allowed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (43, 19, 13)

        # Game speed-up settings
        self.speedup_scale = 1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)