import cocos

from cocos.menu import MenuItem, Menu

import src.core.modules.game_manager

class LooseMenuLayer(Menu):
    """
        'You loose' screen
    """

    def __init__(self):
        super(LooseMenuLayer, self).__init__("YOU LOOSE")

        menu_items = []
        menu_items.append(MenuItem('Restart', on_restart))
        menu_items.append(MenuItem('Quit', on_quit))
        self.create_menu(menu_items, cocos.menu.zoom_in(), cocos.menu.zoom_out())

def on_restart():
    """
        Restart game
    """

    src.core.modules.game_manager.GameManager.restart()

def on_quit():
    """
        Quit game
    """

    src.core.modules.game_manager.GameManager.quit()
