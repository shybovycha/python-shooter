from src.core.modules.base_scene import BaseScene
from src.enemies.sine_enemy import SineEnemy
from src.core.modules.sprite import Sprite

class Level2(BaseScene):
    def __init__(self):
        super(Level2, self).__init__()

    def enemy_waves(self):
        waves = []

        window_width, _ = Sprite.window_size()
        enemy1 = SineEnemy()
        enemy1.health = 150
        enemy1.set_position(window_width + 10, 220)

        enemy2 = SineEnemy()
        enemy1.health = 150
        enemy2.set_position(window_width + 50, 350)

        wave1 = [enemy1, enemy2]
        waves.append(wave1)

        return waves
