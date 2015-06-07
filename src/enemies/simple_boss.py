import math

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.shooting_sprite import ShootingSprite
from src.core.modules.sprite import Sprite
from src.core.modules.missle import Missle
from src.core.modules.enemy import Enemy

class SimpleBoss(Enemy):
    def __init__(self):
        image = ResourceManager.get_boss_image()

        super(SimpleBoss, self).__init__(image)

        self.hit_damage = 100
        self.health = 100
        self.tau = 0

        window_width, window_height = Sprite.window_size()

        self.start_x = window_width - 50
        self.start_y = None

        self.shooting_positions = [ 25, 150, 300, 425, 500, 550, 650, 750, 900 ]

    def update(self, delta_time=1.0):
        if not self.is_alive():
            #self.die()
            return

        self.move()

        shoot_threshold = 3.0
        self_y = self.get_y()

        if min([ abs(self_y - shoot_y) for shoot_y in self.shooting_positions ]) < shoot_threshold:
           self.shoot()

    def move(self, delta_time=1.0):
        if self.get_x() > self.start_x:
            super(SimpleBoss, self).move(delta_time)

        if self.start_y is None:
            self.start_y = self.get_y()

        self.tau += delta_time / 125.0

        if self.tau > math.pi * 2:
            self.tau = 0

        dy = math.sin(self.tau) * 150

        self.set_y(self.start_y + dy)
