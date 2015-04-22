import cocos
from cocos.actions import *

class Sprite(object):
    @staticmethod
    def window_size():
        return cocos.director.director.get_window_size()

    def __init__(self, image, x = 0, y = 0, rotation = 0, anchor = (0, 0), bound_to_window = False):
        self.sprite = cocos.sprite.Sprite(image)
        self.sprite.position = x, y
        self.sprite.rotation = rotation
        self.sprite.anchor = anchor
        self.bound_to_window = bound_to_window
        self.window_size = Sprite.window_size()

    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height

    def set_position(self, x, y):
        if self.bound_to_window:
            x = min(max(x, self.sprite.width / 2), self.window_size[0] - self.sprite.width / 2)
            y = min(max(y, self.sprite.height / 2), self.window_size[1] - self.sprite.height / 2)

        self.sprite.position = x, y

    def set_x(self, x):
        _, y = self.position()
        self.set_position(x, y)

    def set_y(self, y):
        x, _ = self.position()
        self.set_position(x, y)

    def position(self):
        return self.sprite.position

    def x(self):
        return self.sprite.position[0]

    def y(self):
        return self.sprite.position[1]