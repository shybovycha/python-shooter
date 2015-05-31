from src.core.modules.destroyable_entity import DestroyableEntity
from src.core.modules.collidable_particle_system import CollidableParticleSystem

class DestroyableSprite(CollidableParticleSystem, DestroyableEntity):
    """
        Represents sprite, which may both give and take damage when hit.
        This one may die.
    """

    def __init__(self, radius):
        CollidableParticleSystem.__init__(self, radius)
        DestroyableEntity.__init__(self, self.radius)
