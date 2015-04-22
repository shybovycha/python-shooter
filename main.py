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

class Player(CollidableSprite):
    def __init__(self):
        super(Player, self).__init__('resources/ships/spaceship1_final.png', rotation = 90, bound_to_window = True)

class PlayerLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(PlayerLayer, self).__init__()

        self.player = Player()
        self.add(self.player.sprite)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.set_position(x, y)

class BackgroundLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(BackgroundLayer, self).__init__()

        self.parallax_layer = ParallaxLayer('resources/backgrounds/space1.png')

        self.add(self.parallax_layer.bg_img1.sprite)
        self.add(self.parallax_layer.bg_img2.sprite)

    def _step(self, dt):
        self.parallax_layer.shift_background(dt)

class MainScene(cocos.scene.Scene):
    def __init__(self):
        super(MainScene, self).__init__()

    def on_enter(self):
        super(MainScene, self).on_enter()

        self.load_map()
        self.load_players()

    def load_map(self):
        self.background_layer = BackgroundLayer()
        self.add(self.background_layer)

    def load_players(self):
        self.player_layer = PlayerLayer()
        self.add(self.player_layer)

if __name__ == "__main__":
    cocos.director.director.init()

    main_scene = MainScene()

    cocos.director.director.run(main_scene)
