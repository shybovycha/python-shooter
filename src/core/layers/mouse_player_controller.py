from pyglet.window import mouse

from src.core.layers.player_layer import PlayerLayer

class MousePlayerController(PlayerLayer):
    """
        Layer, containing and controlling players (with mouse).
    """

    def __init__(self):
        super(MousePlayerController, self).__init__()

    def on_mouse_motion(self, x_pos, y_pos, _dx, _dy):
        """
            Moving player. Just moving.
        """

        self.player.set_position(x_pos, y_pos)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """
            Moving and shooting.
        """

        self.on_mouse_motion(x, y, dx, dy)
        self.on_mouse_press(x, y, buttons, modifiers)

    def on_mouse_press(self, _x, _y, buttons, _modifiers):
        """
            Shooting. Just shooting.
        """

        if buttons & mouse.LEFT:
            self.player.shoot()
