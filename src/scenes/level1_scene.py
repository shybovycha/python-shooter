import cocos
from cocos.actions import *

from ..layers.background_layer import BackgroundLayer
from ..layers.player_layer import PlayerLayer

class Level1Scene(cocos.scene.Scene):
    def __init__(self):
        super(Level1Scene, self).__init__()

    def on_enter(self):
        super(Level1Scene, self).on_enter()

        self.load_map()
        self.load_players()

    def load_map(self):
        self.background_layer = BackgroundLayer()
        self.add(self.background_layer)

    def load_players(self):
        self.player_layer = PlayerLayer()
        self.add(self.player_layer)