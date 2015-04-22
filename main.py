import cocos
from cocos.actions import *

from src.scenes.level1_scene import Level1Scene

if __name__ == "__main__":
    cocos.director.director.init()

    level1_scene = Level1Scene()

    cocos.director.director.run(level1_scene)
