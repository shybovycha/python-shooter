class ScoreManager(object):
    """
        This is useless class for tracking some points.
    """

    @staticmethod
    def get_enemy_score(enemy):
        """
            Returns amount of points, gained by a player
            for destroying each particular enemy.
        """

        return enemy.health / 10

    @staticmethod
    def get_bonus_score(bonus):
        """
            Returns amount of points, which will be gained by a player
            when he collects the bonus.

            * for missles damage upgrade - 5
            * for missles speed upgrade - 5
            * for health upgrade - 10
            * for nuclear blast upgrade - 25
        """

        pass