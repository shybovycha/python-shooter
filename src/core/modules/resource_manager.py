import random

class ResourceManager(object):
    @staticmethod
    def get_player_image():
        return 'resources/ships/player%d.png' % random.randint(1, 2)

    @staticmethod
    def get_enemy_image():
        return 'resources/ships/enemy%d.png' % random.randint(1, 5)

    @staticmethod
    def get_boss_image():
        return 'resources/ships/boss%d.png' % random.randint(1, 5)
