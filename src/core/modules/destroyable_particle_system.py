from src.core.modules.destroyable_entity import DestroyableEntity
from src.core.modules.collidable_particle_system import CollidableParticleSystem
from src.core.modules.space_explosion import SpaceExplosion

class DestroyableParticleSystem(CollidableParticleSystem, DestroyableEntity):
    """
        Represents sprite, which may both give and take damage when hit.
        This one may die.
    """

    def __init__(self, radius):
        CollidableParticleSystem.__init__(self, radius)
        DestroyableEntity.__init__(self, self.radius)

        self.detonate = False
        self.was_destroyed = False

    def die(self):
        """
            Extend default `die` method to remove the correct
            entity from a layer and create an awesome explosion FX!
        """

        if self.was_destroyed:
            return

        DestroyableEntity.die(self)
        self.kill()

        self.was_destroyed = True