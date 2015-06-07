from src.core.modules.collidable_entity import CollidableEntity
from src.core.modules.collision_manager import CollisionManager
from src.core.modules.space_explosion import SpaceExplosion

class DestroyableEntity(CollidableEntity):
    """
        Represents entity, which may both give and take damage when hit.
        This one may die.
    """

    def __init__(self, radius):
        super(DestroyableEntity, self).__init__(radius)

        self.health = 1
        self.hit_damage = 0
        self.armor = None
        self.detonate = False

    def die(self):
        """
            Cool and fast method to destroy something.
        """

        self.health = 0

        CollisionManager.unregister(self)

        if self.detonate:
            layer = self.sprite.parent
            explosion = SpaceExplosion()
            explosion.position = self.get_position()
            layer.add(explosion)

    def is_alive(self):
        """
            Checks if entity is still alive and should be displayed.
        """

        return self.health > 0

    def on_hit_entity(self, entity):
        """
            When a destroyable entity hits another entity, both take damage.
        """

        self.take_damage(entity.hit_damage)
        entity.take_damage(self.hit_damage)

    def take_damage(self, damage):
        """
            When a destroyable entity hits enemy or missle,

            * when one has armor - armor absorbs some part of damage
            * when one has no armor - full damage is taken
        """

        if self.armor is not None:
            self.health -= self.armor.absorb(damage)
        else:
            self.health -= damage

    def set_armor(self, armor):
        """
            Armors are replaced, not combined.
        """

        self.armor = armor
