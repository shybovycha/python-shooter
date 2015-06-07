import cocos

from cocos.menu import *

from src.core.modules.parallax_layer import ParallaxLayer
from src.core.modules.resource_manager import ResourceManager

import src.core.modules.game_manager

class WinMenuLayer(cocos.menu.Menu):
    def __init__(self):
        super(WinMenuLayer, self).__init__("YOU WIN")

        menu_items = []
        menu_items.append(MenuItem('Once again!', self.on_restart))
        menu_items.append(MenuItem('Quit', self.on_quit))
        self.create_menu(menu_items, zoom_in(), zoom_out())

    def on_restart(self):
        pass

    def on_quit(self):
        src.core.modules.game_manager.GameManager.quit()