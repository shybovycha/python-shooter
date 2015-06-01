import cocos

from cocos.menu import *

from src.core.modules.parallax_layer import ParallaxLayer
from src.core.modules.resource_manager import ResourceManager
from src.core.layers.loose_menu_layer import LooseMenuLayer

class LooseScene(cocos.scene.Scene):
    def __init__(self):
        super(LooseScene, self).__init__()

        loose_menu = LooseMenuLayer()
        self.add(loose_menu)
