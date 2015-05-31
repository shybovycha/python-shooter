import math

from src.core.modules.sprite import Sprite
from src.core.modules.collision_manager import CollisionManager
from src.core.modules.collidable_entity import CollidableEntity

class CollidableSprite(Sprite, CollidableEntity):
    """
        Describes sprite with collision detection.
        Collision shape is just a circle and collision detection
        is just a test if two circles do touch or overlap.
        Radius of a collision circle is the maximum dimension of
        sprite' image.
    """

    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        Sprite.__init__(self,
                        image_path,
                        position=position,
                        rotation=rotation,
                        bound_to_window=bound_to_window)

        radius = max(self.sprite.width / 2, self.sprite.height / 2)

        CollidableEntity.__init__(self, radius)
