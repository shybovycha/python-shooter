import cocos

from cocos.scenes import *

from src.scenes.main_menu_scene import MainMenuScene
from src.scenes.win_scene import WinScene
from src.scenes.loose_scene import LooseScene

class GameManager(object):
    levels = []
    started = False
    current_level = 0

    @classmethod
    def init(self):
        cocos.director.director.init()
        self.levels = [ MainMenuScene() ]

    @classmethod
    def add_level(self, level):
        self.levels.append(level)

    @classmethod
    def start(self):
        self.levels.append(WinScene())
        self.next_level()

    @classmethod
    def next_level(self):
        if not self.started:
            self.started = True
            self.current_level = 0
            level = self.levels[self.current_level]
            cocos.director.director.run(level)
        else:
            self.current_level += 1
            level = self.levels[self.current_level]
            cocos.director.director.replace(level)

    @classmethod
    def restart(self):
        self.current_level = 0
        level = self.levels[self.current_level]
        cocos.director.director.replace(FadeTRTransition(level, duration=1))

    @classmethod
    def quit(self):
        cocos.director.director.pop()