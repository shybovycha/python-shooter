import cocos

from cocos.menu import *

from src.core.modules.parallax_layer import ParallaxLayer
from src.core.modules.resource_manager import ResourceManager

import src.core.modules.game_manager

class LooseMenuLayer(cocos.menu.Menu):
    def __init__(self):
        super(LooseMenuLayer, self).__init__()

        menu_items = []
        menu_items.append(MenuItem('Restart', self.on_restart))
        menu_items.append(MenuItem('Quit', self.on_quit))
        self.create_menu(menu_items, zoom_in(), zoom_out())

    def on_restart(self):
        pass

    def on_quit(self):
        pass