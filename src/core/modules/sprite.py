import cocos

class Sprite(object):
    """
        Base class for almost all the entities you see on the screen.
    """

    @staticmethod
    def window_size():
        """
            Helper method. Needed to place sprites in the meaningful
            places beyond the screen.
        """

        return cocos.director.director.get_window_size()

    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        self.sprite = cocos.sprite.Sprite(image_path)
        self.sprite.position = position
        self.sprite.rotation = rotation
        self.sprite.anchor = (0, 0)
        self.bound_to_window = bound_to_window
        self._window_size = Sprite.window_size()

    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height

    def set_position(self, x_pos, y_pos):
        if self.bound_to_window:
            x_pos = max(x_pos, self.sprite.width / 2)
            x_pos = min(x_pos, self._window_size[0] - self.sprite.width / 2)

            y_pos = max(y_pos, self.sprite.height / 2)
            y_pos = min(y_pos, self._window_size[1] - self.sprite.height / 2)

        self.sprite.position = x_pos, y_pos

    def set_x(self, x_pos):
        _, y_pos = self.get_position()
        self.set_position(x_pos, y_pos)

    def set_y(self, y_pos):
        x_pos, _ = self.get_position()
        self.set_position(x_pos, y_pos)

    def get_position(self):
        return self.sprite.position

    def get_x(self):
        return self.sprite.position[0]

    def get_y(self):
        return self.sprite.position[1]
