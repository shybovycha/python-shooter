import cocos

from src.core.modules.game_manager import GameManager
from src.scenes.level1 import Level1
from src.scenes.level2 import Level2

if __name__ == "__main__":
    GameManager.init()
    GameManager.add_level(Level1())
    GameManager.add_level(Level2())
    GameManager.start()