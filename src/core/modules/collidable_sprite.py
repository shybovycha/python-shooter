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

        """
        image_data = self.sprite.image.get_image_data()
        cols, rows = image_data.width, image_data.height

        # return the alpha component of pixels; store image_data.width bytes per data row
        pixel_data = image_data.get_data('A', cols)

        min_x, max_x, min_y, max_y = cols, 0, rows, 0

        for r in range(0, rows):
            has_non_transparents = False

            for c in range(0, cols):
                if pixel_data[(r * cols) + c] > 0:
                    has_non_transparents = True

                    if c < min_x:
                        min_x = c

                    if c > max_x:
                        max_x = c

            if has_non_transparents:
                if r < min_y:
                    min_y = r

                if r > max_y:
                    max_y = r

        width, height = max_x - min_x, max_y - min_y

        self.radius = max(width / 2, height / 2)
        self.image.image_anchor = (min_x + self.radius, min_y + self.radius)
        """

        self.radius = max(self.sprite.width / 2, self.sprite.height / 2)

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
