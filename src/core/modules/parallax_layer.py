from src.core.modules.sprite import Sprite

class ParallaxLayer(object):
    """Class representing any background, scrolled in time. Endless scrolling..."""

    def __init__(self, image_path):
        self.bg_img1 = Sprite(image_path)
        self.bg_img2 = Sprite(image_path)
        self.bg_img2.set_x(self.bg_img1.width())

        self.bg_img1.set_y(self.bg_img1.height() / 2)
        self.bg_img2.set_y(self.bg_img2.height() / 2)

    def shift_background(self, delta_time=1.0):
        """This method is something like onTimer handler."""

        scroll_speed = 6.0
        delta = scroll_speed * 0.3 * int(delta_time * 100)
        padding_zone = scroll_speed * 5

        self.bg_img1.set_x(self.bg_img1.get_x() - delta)
        self.bg_img2.set_x(self.bg_img2.get_x() - delta)

        win_width, win_height = Sprite.window_size()

        if self.bg_img1.get_x() < -self.bg_img1.width() + win_width + padding_zone:
            self.bg_img2.set_x(self.bg_img1.get_x() + self.bg_img1.width())

            tmp = self.bg_img1
            self.bg_img1 = self.bg_img2
            self.bg_img2 = tmp
