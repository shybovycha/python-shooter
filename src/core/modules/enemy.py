from src.core.modules.resource_manager import ResourceManager
from src.core.modules.shooting_sprite import ShootingSprite
from src.core.modules.missle import Missle

class Enemy(ShootingSprite):
    def __init__(self, image=None):
        if image is None:
            image = ResourceManager.get_enemy_image()

        super(Enemy, self).__init__(image, rotation=-90)

        self.hit_damage = 100

    def update(self, delta_time=1.0):
        if not self.is_alive():
            self.die()
            return

        self.move()

    def move(self, delta_time=1.0):
        move_speed = 3.0
        delta = move_speed * 0.3 * int(delta_time) # * 100)

        self.set_x(self.get_x() - delta)

    def on_hit_entity(self, other):
        if type(self) == type(other):
            return

        self.take_damage(other.hit_damage)

        if not self.is_alive():
            self.die()
