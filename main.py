import cocos
from cocos.actions import *

class Player(object):
    def __init__(self, parent_layer):
        self.window_size = cocos.director.director.get_window_size()
        self.parent_layer = parent_layer
        self.sprite = cocos.sprite.Sprite('resources/ships/spaceship1_final.png')
        self.sprite.rotation = 90
        self.parent_layer.add(self.sprite)

    def move_to(self, x, y):
        x = min(max(x, self.sprite.width / 2), self.window_size[0] - self.sprite.width / 2)
        y = min(max(y, self.sprite.height / 2), self.window_size[1] - self.sprite.height / 2)

        self.sprite.position = x, y

class PlayerLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True

    def __init__(self, scene):
        super(PlayerLayer, self).__init__()

        self.scene = scene
        self.player = Player(self)

    def _step(self, dt):
        self.scene.shift_background()

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.move_to(x, y)

        # self.scene.background.x -= delta
        # self.scene.secondary_background.x -= delta
        # self.scene.background.origin_x -= dx
        # self.scene.scroll_mgr.set_focus(x, y)

class MainScene(cocos.scene.Scene):
    def __init__(self):
        super(MainScene, self).__init__()

        # self.scroll_mgr = cocos.layer.ScrollingManager()
        # self.add(self.scroll_mgr)

    def on_enter(self):
        super(MainScene, self).on_enter()

        self.load_map()
        self.load_players()

    def shift_background(self):
        scroll_speed = 7.0
        delta = scroll_speed * 0.3
        padding_zone = scroll_speed * 5

        self.bg_img1.x -= delta
        self.bg_img2.x -= delta

        win_width, win_height = cocos.director.director.get_window_size()

        if self.bg_img1.x < -self.bg_img1.width + win_width + padding_zone:
            self.bg_img2.x = self.bg_img1.x + self.bg_img1.width

            tmp = self.bg_img1
            self.bg_img1 = self.bg_img2
            self.bg_img2 = tmp

    def load_map(self):
        # self.background = cocos.layer.ScrollableLayer()
        self.background = cocos.layer.Layer()

        self.bg_img1 = cocos.sprite.Sprite('resources/backgrounds/space1.png', anchor = (0, 0))
        self.bg_img2 = cocos.sprite.Sprite('resources/backgrounds/space1.png', anchor = (0, 0))
        self.bg_img2.x = self.bg_img1.width

        self.background.add(self.bg_img1)
        self.background.add(self.bg_img2)
        # self.background.parallax = 0
        self.background.x = 0
        self.background.y = 0

        self.add(self.background)

        # self.scroll_mgr.add(self.background, z = -1)

    def load_players(self):
        self.player_layer = PlayerLayer(self)
        self.add(self.player_layer)

        # self.scroll_mgr.add(self.player_layer, z = 100)

if __name__ == "__main__":
    cocos.director.director.init()

    main_scene = MainScene()

    cocos.director.director.run(main_scene)
