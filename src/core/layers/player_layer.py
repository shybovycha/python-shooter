import cocos

from src.core.modules.player import Player
from src.core.modules.sprite import Sprite
from src.core.modules.collision_manager import CollisionManager

class PlayerLayer(cocos.layer.Layer):
    """
        Layer, containing and controlling players.
    """

    is_event_handler = True

    def __init__(self):
        super(PlayerLayer, self).__init__()

        self.player = Player()
        self.add(self.player.sprite)
        CollisionManager.register(self.player)

    def _step(self, delta_time):
        """
            Called each frame. This is a good place to
            update all player' missles.
        """

        CollisionManager.update()

        _missles = self.player.alive_missles()
        padding = 80
        screen_width, screen_height = Sprite.window_size()

        for missle in _missles:
            if missle.get_x() > screen_width + padding or missle.get_x() < 0:
                missle.die(detonate=False)

            missle.update(delta_time)