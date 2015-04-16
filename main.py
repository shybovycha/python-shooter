import cocos
from cocos.actions import *

class Player(object):
    def __init__(self, parent_layer):
        self.window_size = cocos.director.director.get_window_size()
        self.parent_layer = parent_layer
        self.sprite = cocos.sprite.Sprite('resources/ships/spaceship1_final.png')
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

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.move_to(x, y)

        scroll_speed = 3.0
        self.scene.background.y -= scroll_speed * 0.3
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

    def load_map(self):
        # self.background = cocos.layer.ScrollableLayer()
        self.background = cocos.layer.Layer()

        image = cocos.sprite.Sprite('resources/backgrounds/space1.png', anchor = (0, 0))

        self.background.add(image)
        self.background.parallax = 0
        self.background.x = 0 #-image.width / 2
        self.background.y = 0 #image.height

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
