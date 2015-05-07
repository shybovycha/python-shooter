from src.core.modules.destroyable_entity import DestroyableEntity

class Missle(DestroyableEntity):
    """
        When missles are launched, no one can hide!
    """

    def __init__(self, image, parent=None, damage=1, speed=10):
        if parent is Player:
            rotation = 90
            direction = 1
        elif parent is Enemy:
            rotation = -90
            direction = -1

        super(Missle, self).__init__(image, rotation=rotation)

        self.parent = parent
        self.health = 1
        self.hit_damage = damage
        self.speed = speed
        self.direction = direction

    def on_hit_entity(self, entity):
        """
            When one goes through its friend, it does not blow-up.
        """

        if type(entity).__name__ != type(self.parent).__name__:
            self.die()

    def update(self, delta_time=1.0):
        self.move(delta_time)

    def move(self, delta_time=1.0):
        """
            Move missle in its direction.
        """

        delta = self.direction * self.speed * 0.3 * int(delta_time * 100)

        self.set_x(self.x() + delta)
