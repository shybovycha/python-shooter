import cocos

from src.core.layers.main_menu_layer import MainMenuLayer

class MainMenuScene(cocos.scene.Scene):
    """
        Main menu
    """

    def __init__(self):
        super(MainMenuScene, self).__init__()

        self.menu_layer = MainMenuLayer()
        self.add(self.menu_layer)
