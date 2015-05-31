from src.core.modules.destroyable_entity import DestroyableEntity
from src.core.modules.missle import Missle

class ShootingEntity(DestroyableEntity):
    def __init__(self, radius):
        super(ShootingEntity, self).__init__(radius)

        self.missles = []
        self.missle_damage = 1
        self.missle_speed = 15.0

    def shoot(self):
        missle = Missle(parent=self, damage=self.missle_damage, speed=self.missle_speed)
        self.missles.append(missle)
