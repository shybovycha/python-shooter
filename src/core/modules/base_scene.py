import cocos

from src.core.layers.background_layer import BackgroundLayer
from src.core.layers.mouse_player_controller import MousePlayerController
from src.core.layers.enemy_layer import EnemyLayer
from src.core.layers.status_bar_layer import StatusBarLayer

class BaseScene(cocos.scene.Scene):
    """
        Base class for scenes. Encapsulates player(-s)
        loading and enemies loading.
        Enemy deploys (waves) are handled by EnemyLayer.
    """

    def __init__(self):
        super(BaseScene, self).__init__()

        self.background_layer = None
        self.player_layer = None
        self.enemies_layer = None
        self.status_bar_layer = None
        self.saved_player = None

    def on_enter(self):
        """
            When scene was just loaded.
        """

        super(BaseScene, self).on_enter()

        self.load_map()
        self.load_players()
        self.load_enemies()
        self.load_status_bar()

        self.enemies_layer.next_wave()

    def load_map(self, background_image=None):
        """
            Just loads the background layer.
        """

        self.background_layer = BackgroundLayer(background_image)
        self.add(self.background_layer)

    def load_players(self):
        """
            Sets up players' layer.
        """

        self.player_layer = MousePlayerController()
        self.player_layer.player.push_handlers(self)
        self.add(self.player_layer)

        if self.saved_player is not None:
            self.player_layer.player.set_params(self.saved_player)

    def get_player(self):
        """
            Returns player
        """

        return self.player_layer.player.get_params()

    def set_player(self, player_params):
        """
            Sets new player. Used to restore player on level transition
        """

        self.saved_player = player_params

    def load_enemies(self):
        """
            Sets up the enemies layer and fills it with enemy waves.
        """

        self.enemies_layer = EnemyLayer()
        self.enemies_layer.set_enemy_waves(self.enemy_waves())
        self.enemies_layer.push_handlers(self)
        self.add(self.enemies_layer)

    def load_status_bar(self):
        """
            Loads the status bar layer.
        """

        self.status_bar_layer = StatusBarLayer(self.player_layer.player)
        self.add(self.status_bar_layer)

    def on_next_wave(self, wave_index, waves_cnt):
        """
            Handles 'next_wave' event.
        """

        self.status_bar_layer.set_wave(wave_index, waves_cnt)

    def on_player_hit(self, player):
        """
            Handles 'player.on_hit' event.
        """

        self.status_bar_layer.set_player_state(player)

    def enemy_waves(self):
        """
            To be implemented in each scene class.
        """

        pass
