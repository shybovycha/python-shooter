from src.core.modules.destroyable_sprite import DestroyableSprite
from src.core.modules.player import Player

class Bonus(DestroyableSprite):
    """
        Represents abstract bonus.
    """

    def __init__(self, image_path, position=(0, 0)):
        super(Bonus, self).__init__(image_path, position, rotation=0, bound_to_window=False)

        self.health = 1
        self.hit_damage = 0
        self.detonate = False
        self.movement_speed = 3.0

    def affect(self, player):
        """
            To be implemented in ancesing classes.
        """

        pass

    def on_hit_entity(self, other):
        """
            Override default collision handling.
        """

        if not isinstance(other, Player):
            return

        self.affect(other)

        self.die()

    def update(self, delta_time):
        """
            Override default method to just move
            the bonus along level towards player.
        """

        delta = self.movement_speed * 0.3 * int(delta_time)

        self.set_x(self.get_x() - delta)