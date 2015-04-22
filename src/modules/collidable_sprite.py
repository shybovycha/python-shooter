import cocos
from cocos.actions import *
from sprite import Sprite

class CollidableSprite(Sprite):
    def __init__(self, image, x = 0, y = 0, rotation = 0, anchor = (0, 0), bound_to_window = False):
        super(CollidableSprite, self).__init__(image, x = x, y = y, rotation = rotation, anchor = anchor, bound_to_window = bound_to_window)

        self.radius = max(self.sprite.width, self.sprite.height)

    def _distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def check_collision(self, other):
        d = self._distance(self.x, self.y, other.x, other.y)
        r1, r2 = self.radius, other.radius

        if (d <= r1 + r2):
            return True
        else:
            return False