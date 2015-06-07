class Armor(object):
    """
        Class representing armor.
        Armor absorbs some damage, reducing damage for player.
    """

    def __init__(self, absorb_coeff=0.5, health=100):
        self.absorb_coeff = absorb_coeff
        self.health = health
        self.max_health = health

    def absorb(self, damage):
        """
            Absorbed damage may destroy armor itself.
            So, let's stay alive as much as we can to save our Master!
        """

        delta = min(self.health, damage) * self.absorb_coeff
        self.health = int(self.health - delta)
        return 1.0 - delta