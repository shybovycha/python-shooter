import cocos

from cocos.menu import MenuItem, Menu

import src.core.modules.game_manager

class WinMenuLayer(Menu):
    """
        'You win' screen
    """

    def __init__(self):
        super(WinMenuLayer, self).__init__("YOU WIN")

        menu_items = []
        menu_items.append(MenuItem('Once again!', on_restart))
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
