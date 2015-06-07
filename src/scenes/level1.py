import cocos

from src.core.modules.sprite import Sprite
from src.core.modules.base_scene import BaseScene

from src.enemies.sine_enemy import SineEnemy

from src.bonuses.armor_bonus import ArmorBonus
from src.bonuses.damage_bonus import DamageBonus

class Level1(BaseScene):
    def __init__(self):
        super(Level1, self).__init__()

    def enemy_waves(self):
        waves = []

        window_width, window_height = Sprite.window_size()
        enemy1 = SineEnemy()
        enemy1.set_position(window_width + 10, 220)
        enemy1.bonus_classes = [ ArmorBonus ]

        enemy2 = SineEnemy()
        enemy1.health = 50
        enemy2.set_position(window_width + 50, 350)

        wave1 = [enemy1, enemy2]
        waves.append(wave1)

        return waves