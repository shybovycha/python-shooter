import math

from cocos.particle import ParticleSystem
from src.core.modules.collision_manager import CollisionManager
from src.core.modules.collidable_entity import CollidableEntity

class CollidableParticleSystem(ParticleSystem, CollidableEntity):
    """
        Describes particle system with collision detection.
        Collision shape is just a circle and collision detection
        is just a test if two circles do touch or overlap.
        Radius of a collision circle is set manually.
    """

    def __init__(self, radius):
        ParticleSystem.__init__(self)
        CollidableEntity.__init__(self, radius)

        self.radius = radius

    def rgb2color(r, g, b, a = 255.0):
        """
            Utilizes some helper methods for particle systems.
        """

        return Color(r / 255.0, g / 255.0, b / 255.0, a / 255.0)