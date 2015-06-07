import cocos

from src.core.layers.loose_menu_layer import LooseMenuLayer

class LooseScene(cocos.scene.Scene):
    def __init__(self):
        super(LooseScene, self).__init__()

        loose_menu = LooseMenuLayer()
        self.add(loose_menu)
