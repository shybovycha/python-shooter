import cocos

from cocos.menu import *

from src.core.modules.parallax_layer import ParallaxLayer
from src.core.modules.resource_manager import ResourceManager

import src.core.modules.game_manager

class MainMenuLayer(cocos.menu.Menu):
    def __init__(self):
        super(MainMenuLayer, self).__init__()

        menu_items = []
        menu_items.append(MenuItem('Start', self.on_new_game))
        menu_items.append(MenuItem('Quit', self.on_quit))
        self.create_menu(menu_items, zoom_in(), zoom_out())

    def on_new_game(self):
        src.core.modules.game_manager.GameManager.next_level()

    def on_quit(self):
        src.core.modules.game_manager.GameManager.quit()
