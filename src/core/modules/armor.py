class Armor(object):
    def __init__(self, absorb_coeff=0.5, health=100):
        self.absorb_coeff = absorb_coeff
        self.health = health

    def absorb(self, damage):
        delta = min(self.health, damage) * self.absorb_coeff
        self.health -= delta
        return 1.0 - delta