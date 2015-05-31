from src.core.modules.destroyable_entity import DestroyableEntity

class Missle(DestroyableEntity):
    """
        When missles are launched, no one can hide!
    """

    def __init__(self, radius, owner=None, damage=1, speed=10, direction=1):
        super(Missle, self).__init__(radius)

        self.owner = owner
        self.health = 1
        self.hit_damage = damage
        self.speed = speed
        self.direction = direction

        if owner is not None:
            self.set_position(owner.get_x(), owner.get_y())

    def on_hit_entity(self, entity):
        """
            When one goes through its friend, it does not blow-up.
        """

        if type(entity).__name__ != type(self.owner).__name__:
            entity.take_damage(self.hit_damage)
            self.die(detonate=False)

    def update(self, delta_time=1.0):
        """
            This missle is not artifical enough to move anywhere but forward.
        """

        self.move(delta_time)

    def move(self, delta_time=1.0):
        """
            Move missle in its direction.
        """

        delta = self.direction * self.speed * 0.3 * int(delta_time * 100)

        self.set_x(self.get_x() + delta)

    def die(self):
        """
            Just remove itself.
        """

        DestroyableEntity.die(self)

        self.owner.missles.remove(self)