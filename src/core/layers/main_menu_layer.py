import cocos

from cocos.menu import MenuItem, Menu
from cocos.text import Label

import src.core.modules.game_manager

class MainMenuLayer(Menu):
    """
        Main menu
    """

    def __init__(self):
        super(MainMenuLayer, self).__init__("PySHOOTER")

        menu_items = []
        menu_items.append(MenuItem('Start', self.on_new_game))
        menu_items.append(MenuItem('Quit', self.on_quit))
        self.create_menu(menu_items, cocos.menu.zoom_in(), cocos.menu.zoom_out())

    def on_new_game(self):
        """
            Starts new game
        """

        src.core.modules.game_manager.GameManager.next_level()

    def on_quit(self):
        """
            Quit game
        """

        src.core.modules.game_manager.GameManager.quit()
