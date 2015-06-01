import cocos

from cocos.menu import *

from src.core.modules.parallax_layer import ParallaxLayer
from src.core.modules.resource_manager import ResourceManager
from src.core.layers.win_menu_layer import WinMenuLayer

class WinScene(cocos.scene.Scene):
    def __init__(self):
        super(WinScene, self).__init__()

        win_menu = WinMenuLayer()
        self.add(win_menu)
