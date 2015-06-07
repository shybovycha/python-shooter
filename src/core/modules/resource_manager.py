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

    @staticmethod
    def get_repair_bonus_image():
        """
            Get repair bonus image
        """

        return 'resources/bonuses/health1.gif'

    @staticmethod
    def get_damage_bonus_image():
        """
            Get damage bonus image
        """

        return 'resources/bonuses/gun5.png'

    @staticmethod
    def get_armor_bonus_image():
        """
            Get armor bonus image
        """

        return 'resources/bonuses/armor4.png'
