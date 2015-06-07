import math

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.enemy import Enemy

class SineEnemy(Enemy):
    """
        Stupid enemy
    """

    def __init__(self):
        image = ResourceManager.get_enemy_image()

        super(SineEnemy, self).__init__(image)

        self.hit_damage = 100
        self.health = 100
        self.tau = 0
        self.start_y = None

    def update(self, _delta_time=1.0):
        """
            Only made for moving along a sine wave
        """

        if not self.is_alive():
            return

        self.move()

        if (self.get_y() > 250 or self.get_y() < 50) and int(self.get_y()) % 25 == 0:
            self.shoot()

    def move(self, delta_time=1.0):
        """
            Still moving towards player
        """

        super(SineEnemy, self).move(delta_time)

        if self.start_y is None:
            self.start_y = self.get_y()

        self.tau += delta_time / 100.0

        if self.tau > math.pi * 2:
            self.tau = 0

        delta_y = math.sin(self.tau) * 50

        self.set_y(self.start_y + delta_y)
