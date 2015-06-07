import cocos

from cocos.scenes import *

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
    def init(self):
        cocos.director.director.init()

        self.level_classes = []
        self.level_classes.append(MainMenuScene)

    @classmethod
    def add_level(self, level_class):
        self.level_classes.append(level_class)

    @classmethod
    def start(self):
        self.level_classes.append(WinScene)
        self.load_levels()
        self.next_level()

    @classmethod
    def load_levels(self):
        self.levels = [ level() for level in self.level_classes ]

    @classmethod
    def next_level(self):
        if not self.started:
            self.started = True
            self.current_level = 0
            level = self.levels[self.current_level]
            cocos.director.director.run(level)
        else:
            player = None

            if self.current_level > 0 and self.current_level < len(self.levels) - 2:
                player = self.levels[self.current_level].get_player()

            self.current_level += 1
            level = self.levels[self.current_level]

            if player is not None:
                level.set_player(player)

            cocos.director.director.replace(level)

    @classmethod
    def restart(self):
        self.load_levels()
        self.current_level = 1
        level = self.levels[self.current_level]
        print("restart", level)
        cocos.director.director.run(level)

    @classmethod
    def loose(self):
        level = LooseScene()
        cocos.director.director.replace(FadeTRTransition(level, duration=1))

    @classmethod
    def quit(self):
        cocos.director.director.pop()