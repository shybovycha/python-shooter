import math
from src.modules.sprite import Sprite

class CollidableSprite(Sprite):
    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        super(CollidableSprite, self).__init__(image_path,
                                               position=position,
                                               rotation=rotation,
                                               bound_to_window=bound_to_window)

        self.radius = max(self.sprite.width, self.sprite.height)

    def _distance(self, point):
        x_pos1, y_pos1 = self.position()
        x_pos2, y_pos2 = point
        return math.sqrt((x_pos1 - x_pos2)**2 + (y_pos1 - y_pos2)**2)

    def check_collision(self, other):
        centers_distance = self._distance(other.position())
        radius1, radius2 = self.radius, other.radius

        if centers_distance <= radius1 + radius2:
            return True
        else:
            return False
