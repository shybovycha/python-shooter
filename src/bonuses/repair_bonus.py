import random

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.bonus import Bonus

class RepairBonus(Bonus):
    """
        Repairs the ship or raises its maximum health.
    """

    def __init__(self, position=(0, 0)):
        image = ResourceManager.get_repair_bonus_image()

        Bonus.__init__(self, image, position)

    def affect(self, player):
        """
            Affect player.
        """

        if player.health >= player.max_health:
            player.max_health += random.randrange(1, 10) * random.randrange(1, 5) * 10

        player.health = player.max_health
