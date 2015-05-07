import cocos

from src.core.modules.player import Player

class PlayerLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(PlayerLayer, self).__init__()

        self.player = Player()
        self.add(self.player.sprite)

    def on_mouse_motion(self, x_pos, y_pos, _dx, _dy):
        self.player.set_position(x_pos, y_pos)
