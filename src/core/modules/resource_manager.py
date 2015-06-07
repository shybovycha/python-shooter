import random

class ResourceManager(object):
    """
        Image dealer.
    """

    @staticmethod
    def get_player_image():
        """
            Gets sample player image.
        """

        return 'resources/ships/player%d.png' % random.randint(1, 2)

    @staticmethod
    def get_enemy_image():
        """
            Gets sample enemy image.
        """

        return 'resources/ships/enemy%d.png' % random.randint(1, 5)

    @staticmethod
    def get_boss_image():
        """
            Returns sample boss image.
        """

        return 'resources/ships/boss%d.png' % random.randint(1, 5)

    @staticmethod
    def get_background_image():
        """
            Provides background image.
        """

        return 'resources/backgrounds/space%d.png' % random.randint(1, 1)
