from src.core.modules.destroyable_entity import DestroyableEntity
from src.core.modules.missle import Missle

class ShootingEntity(DestroyableEntity):
    def __init__(self, image, rotation=0, bound_to_window=False):
        super(ShootingEntity, self).__init__(image, rotation=rotation, bound_to_window=bound_to_window)

        self.missles = []
        self.missle_damage = 1
        self.missle_speed = 15.0

    def shoot(self):
        missle = Missle(parent=self, damage=self.missle_damage, speed=self.missle_speed)
        self.missles.append(missle)
