import random

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.bonus import Bonus
from src.core.modules.armor import Armor

class DamageBonus(Bonus):
    """
        Increase player' damage.
    """

    def __init__(self):
        image = ResourceManager.get_damage_bonus_image()

        Bonus.__init__(self, image, position)

    def affect(self, player):
        """
            Affect player.
        """

        player.damage += random.randrange(1, 10) * 10