from src.core.modules.game_manager import GameManager
from src.scenes.level1 import Level1
from src.scenes.level2 import Level2
from src.scenes.level3 import Level3

class Game(object):
    """
        Class, representing the whole game.
    """

    @classmethod
    def start(cls):
        """
            Init levels.
        """

        GameManager.init()
        GameManager.add_level(Level1)
        GameManager.add_level(Level2)
        GameManager.add_level(Level3)
        GameManager.start()
