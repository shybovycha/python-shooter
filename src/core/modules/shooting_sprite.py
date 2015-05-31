from src.core.modules.destroyable_sprite import DestroyableSprite
from src.core.modules.missle import Missle

class ShootingSprite(DestroyableSprite):
    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        super(ShootingSprite, self).__init__(image_path, position, rotation, bound_to_window)

        self.missles = []
        self.missle_damage = 1
        self.missle_speed = 15.0

    def shoot(self):
        missle = Missle(parent=self, damage=self.missle_damage, speed=self.missle_speed)
        self.missles.append(missle)
