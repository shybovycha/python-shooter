import math

from src.core.modules.sprite import Sprite
from src.core.modules.collision_manager import CollisionManager

class CollidableSprite(Sprite):
    """
        Describes sprite with collision detection.
        Collision shape is just a circle and collision detection
        is just a test if two circles do touch or overlap.
        Radius of a collision circle is the maximum dimension of
        sprite' image.
    """

    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        super(CollidableSprite, self).__init__(image_path,
                                               position=position,
                                               rotation=rotation,
                                               bound_to_window=bound_to_window)

        self.radius = max(self.sprite.width, self.sprite.height)

        CollisionManager.register(self)

    def die(self):
        """
            Disables collision detection for this sprite.
        """

        CollisionManager.unregister(self)

    def _distance(self, point):
        """
            Returns distance from this sprite to another one.
        """

        x_pos1, y_pos1 = self.position()
        x_pos2, y_pos2 = point
        return math.sqrt((x_pos1 - x_pos2)**2 + (y_pos1 - y_pos2)**2)

    def check_collision(self, other):
        """
            Checks if two collision shapes overlap.
        """

        centers_distance = self._distance(other.position())
        radius1, radius2 = self.radius, other.radius

        if centers_distance <= radius1 + radius2:
            return True
        else:
            return False

    def on_hit_entity(self, entity):
        """
            OnCollision handler. To be implemented in each derived class.
        """

        pass
