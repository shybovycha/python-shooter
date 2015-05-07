from src.core.modules.resource_manager import ResourceManager
from src.core.modules.shooting_entity import ShootingEntity
from src.core.modules.missle import Missle

class Enemy(ShootingEntity):
    def __init__(self, image=None):
        if image is None:
            image = ResourceManager.get_enemy_image()

        super(Enemy, self).__init__(image, rotation=-90)

        self.hit_damage = 100

    def update(self, delta_time=1.0):
        self.move()

    def move(self, delta_time=1.0):
        move_speed = 8.0
        delta = move_speed * 0.3 * int(delta_time * 100)

        self.set_x(self.x() - delta)
