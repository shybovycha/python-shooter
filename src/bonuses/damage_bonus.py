import random

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.bonus import Bonus

class DamageBonus(Bonus):
    """
        Increase player' damage.
    """

    def __init__(self, position=(0, 0)):
        image = ResourceManager.get_damage_bonus_image()

        Bonus.__init__(self, image, position)

    def affect(self, player):
        """
            Affect player.
        """

        player.damage += random.randrange(1, 10) * 10
