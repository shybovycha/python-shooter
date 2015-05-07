import cocos

from src.core.layers.background_layer import BackgroundLayer
from src.core.layers.player_layer import PlayerLayer
from src.core.layers.enemy_layer import EnemyLayer

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

    def on_enter(self):
        """
            When scene was just loaded.
        """

        super(BaseScene, self).on_enter()

        self.load_map()
        self.load_players()
        self.load_enemies()

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

        self.player_layer = PlayerLayer()
        self.add(self.player_layer)

    def load_enemies(self):
        """
            Sets up the enemies layer and fills it with enemy waves.
        """

        self.enemies_layer = EnemyLayer()
        self.enemies_layer.set_enemy_waves(self.enemy_waves())
        self.add(self.enemies_layer)

    def enemy_waves(self):
        """
            To be implemented in each scene class.
        """

        pass
