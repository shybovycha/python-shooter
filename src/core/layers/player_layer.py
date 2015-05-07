import cocos

from src.core.modules.player import Player

class PlayerLayer(cocos.layer.Layer):
    """
        Layer, containing and controlling players.

        TODO: implement PlayerController and load either one or more players.
    """

    is_event_handler = True

    def __init__(self):
        super(PlayerLayer, self).__init__()

        self.player = Player()
        self.add(self.player.sprite)

    def on_mouse_motion(self, x_pos, y_pos, _dx, _dy):
        """
            Control player with mouse.
        """

        self.player.set_position(x_pos, y_pos)
