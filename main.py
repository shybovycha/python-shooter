import cocos

from src.scenes.level1 import Level1

if __name__ == "__main__":
    cocos.director.director.init()

    level_scene = Level1()

    cocos.director.director.run(level_scene)
