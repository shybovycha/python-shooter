from src.core.modules.collidable_sprite import CollidableSprite

class DestroyableEntity(CollidableSprite):
    """
        Represents entity, which may both give and take damage when hit.
        This one may die.
    """

    def __init__(self, image_path, rotation=0, health=100, bound_to_window=False):
        super(DestroyableEntity, self).__init__(image_path, rotation=rotation, bound_to_window=bound_to_window)

        self.health = 1
        self.hit_damage = 0
        self.armor = None

    def die(self):
        """
            Cool and fast method to destroy something.
        """

        self.health = 0

    def is_alive(self):
        """
            Checks if entity is still alive and should be displayed.
        """

        return self.health > 0

    def on_hit_entity(self, entity):
        """
            When a destroyable entity hits another entity, both take damage.
        """

        self.take_damage(entity.hit_damage())
        entity.take_damage(self.hit_damage())

    def hit_damage(self):
        """
            Returns the amount of damage, another entity will take when hit this one.
        """

        return self.hit_damage

    def take_damage(self, damage):
        """
            When a destroyable entity hits enemy or missle,

            * when one has armor - armor absorbs some part of damage
            * when one has no armor - full damage is taken
        """

        if self.armor is not None:
            self.health -= damage
        else:
            self.health -= self.armor.absorb(damage)

    def set_armor(self, armor):
        """
            Armors are replaced, not combined.
        """

        self.armor = armor
