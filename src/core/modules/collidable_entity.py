import math

from src.core.modules.collision_manager import CollisionManager

class CollidableEntity():
    """
        Describes entity with collision detection.
        Collision shape is just a circle and collision detection
        is just a test if two circles do touch or overlap.
        Radius of a collision circle is set manually.
    """

    def __init__(self, radius):
        self.radius = radius

    def _distance(self, point):
        """
            Returns distance from this entity to another one.
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
