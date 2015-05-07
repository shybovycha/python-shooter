import cocos

from src.core.layers.background_layer import BackgroundLayer
from src.core.layers.player_layer import PlayerLayer

class Level1(cocos.scene.Scene):
    def __init__(self):
        super(Level1, self).__init__()
        self.background_layer = None
        self.player_layer = None

    def on_enter(self):
        super(Level1, self).on_enter()

        self.load_map()
        self.load_players()

    def load_map(self):
        self.background_layer = BackgroundLayer()
        self.add(self.background_layer)

    def load_players(self):
        self.player_layer = PlayerLayer()
        self.add(self.player_layer)
