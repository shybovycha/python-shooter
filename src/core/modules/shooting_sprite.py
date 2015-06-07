from src.core.modules.destroyable_sprite import DestroyableSprite
from src.core.modules.plasma_ball import PlasmaBall
from src.core.modules.collision_manager import CollisionManager

class ShootingSprite(DestroyableSprite):
    """
        Represents sprite which could shot you down.
    """

    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        super(ShootingSprite, self).__init__(image_path, position, rotation, bound_to_window)

        self.missles = []
        self.missle_damage = 1
        self.missle_speed = 15.0
        self.missle_direction = 1

    def shoot(self):
        """
            The most dangerous method.
        """

        missle = PlasmaBall(owner=self,
                            damage=self.missle_damage,
                            speed=self.missle_speed,
                            direction=self.missle_direction)

        self.missles.append(missle)
        self.sprite.parent.add(missle)
        CollisionManager.register(missle)

    def alive_missles(self):
        """
            All missles, which did not reach their target yet.
        """

        return filter(lambda missle: missle.is_alive(), self.missles)
