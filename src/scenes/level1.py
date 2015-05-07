import cocos

from src.core.modules.base_scene import BaseScene
from src.core.modules.enemy import Enemy

class Level1(BaseScene):
    def __init__(self):
        super(Level1, self).__init__()

    def enemy_waves(self):
        waves = []

        enemy1 = Enemy()
        enemy1.set_y(20)
        enemy2 = Enemy()
        enemy2.set_y(100)

        wave1 = [enemy1, enemy2]
        waves.append(wave1)

        return waves