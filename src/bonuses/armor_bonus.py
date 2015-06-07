import random

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.bonus import Bonus
from src.core.modules.armor import Armor

class ArmorBonus(Bonus):
    """
        Provides ship with a brand new armor!
    """

    def __init__(self, position=(0, 0)):
        image = ResourceManager.get_armor_bonus_image()

        Bonus.__init__(self, image, position)

        absorb_coeff = random.randrange(25, 100) / 100.0
        health = random.randrange(100, 2000)
        self.armor = Armor(absorb_coeff=absorb_coeff, health=health)

    def affect(self, player):
        """
            Set new armor, do not repair existing.
        """

        player.armor = self.armor