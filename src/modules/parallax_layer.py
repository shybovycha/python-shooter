from sprite import Sprite

class ParallaxLayer(object):
    def __init__(self, image):
        self.bg_img1 = Sprite('resources/backgrounds/space1.png')
        self.bg_img2 = Sprite('resources/backgrounds/space1.png')
        self.bg_img2.set_x(self.bg_img1.width())

        self.bg_img1.set_y(self.bg_img1.height() / 2)
        self.bg_img2.set_y(self.bg_img2.height() / 2)

    def shift_background(self, dt = 1.0):
        scroll_speed = 6.0
        delta = scroll_speed * 0.3 * int(dt * 100)
        padding_zone = scroll_speed * 5

        self.bg_img1.set_x(self.bg_img1.x() - delta)
        self.bg_img2.set_x(self.bg_img2.x() - delta)

        win_width, win_height = Sprite.window_size()

        if self.bg_img1.x() < -self.bg_img1.width() + win_width + padding_zone:
            self.bg_img2.set_x(self.bg_img1.x() + self.bg_img1.width())

            tmp = self.bg_img1
            self.bg_img1 = self.bg_img2
            self.bg_img2 = tmp