import cocos

from cocos.menu import MenuItem, Menu

import src.core.modules.game_manager

class MainMenuLayer(Menu):
    """
        Main menu
    """

    def __init__(self):
        super(MainMenuLayer, self).__init__("PySHOOTER")

        menu_items = []
        menu_items.append(MenuItem('Start', on_new_game))
        menu_items.append(MenuItem('Quit', on_quit))
        self.create_menu(menu_items, cocos.menu.zoom_in(), cocos.menu.zoom_out())

def on_new_game():
    """
        Starts new game
    """

    src.core.modules.game_manager.GameManager.next_level()

def on_quit():
    """
        Quit game
    """

    src.core.modules.game_manager.GameManager.quit()
