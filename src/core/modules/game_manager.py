import cocos

from cocos.scenes.transitions import FadeTRTransition

from src.scenes.main_menu_scene import MainMenuScene
from src.scenes.win_scene import WinScene
from src.scenes.loose_scene import LooseScene

class GameManager(object):
    """
        Class which manages level transitions and menu displaying.
    """

    levels = []
    level_classes = []
    started = False
    current_level = 0

    @classmethod
    def init(cls):
        """
            Initializer
        """

        cocos.director.director.init()

        cls.level_classes = []
        cls.level_classes.append(MainMenuScene)

    @classmethod
    def add_level(cls, level_class):
        """
            Add level class to be loaded
        """

        cls.level_classes.append(level_class)

    @classmethod
    def start(cls):
        """
            Start game
        """

        cls.level_classes.append(WinScene)
        cls.load_levels()
        cls.next_level()

    @classmethod
    def load_levels(cls):
        """
            Preload levels
        """

        cls.levels = [level() for level in cls.level_classes]

    @classmethod
    def next_level(cls):
        """
            Start next level
        """

        if not cls.started:
            cls.started = True
            cls.current_level = 0
            level = cls.levels[cls.current_level]
            cocos.director.director.run(level)
        else:
            player = None

            if cls.current_level > 0 and cls.current_level < len(cls.levels) - 2:
                player = cls.levels[cls.current_level].get_player()

            cls.current_level += 1
            level = cls.levels[cls.current_level]

            if player is not None:
                level.set_player(player)

            cocos.director.director.replace(level)

    @classmethod
    def restart(cls):
        """
            Restart game
        """

        cls.load_levels()
        cls.current_level = 1
        level = cls.levels[cls.current_level]
        print("restart", level)
        cocos.director.director.run(level)

    @classmethod
    def loose(cls):
        """
            Loose game
        """

        level = LooseScene()
        cocos.director.director.replace(FadeTRTransition(level, duration=1))

    @classmethod
    def quit(cls):
        """
            Quit game
        """

        cocos.director.director.pop()
