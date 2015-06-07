import cocos

from src.core.modules.base_scene import BaseScene
from src.enemies.simple_boss import SimpleBoss
from src.core.modules.sprite import Sprite

class Level3(BaseScene):
    def __init__(self):
        super(Level3, self).__init__()

    def enemy_waves(self):
        waves = []

        window_width, window_height = Sprite.window_size()

        boss = SimpleBoss()
        boss.health = 1500
        boss.set_position(window_width + 50, window_height / 2)

        wave1 = [ boss ]
        waves.append(wave1)

        return waves