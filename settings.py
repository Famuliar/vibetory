class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.max_meteorites = 1
        self.ship_speed = 8
        self.meteorite_speed = 9
        self.points = 0
        self.aktive = True
        self.bullet_speed = 15  # Bullet speed
        self.max_bullets = 5    # Max bullet count
        self.bullets_left = 5   # Current bullet count
        self.bonus_points = 10  # Points for collecting bonus
        self.bonus_spawn_chance = 100  # 1 in 100 chance per frame