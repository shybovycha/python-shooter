from cocos.particle import ParticleSystem

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

    def set_position(self, x_pos, y_pos):
        self.position = x_pos, y_pos

    def set_x(self, x_pos):
        _, y_pos = self.position
        self.position = x_pos, y_pos

    def set_y(self, y_pos):
        x_pos, _ = self.position
        self.position = x_pos, y_pos

    def get_x(self):
        x_pos, _ = self.position
        return x_pos

    def get_y(self):
        _, y_pos = self.position
        return y_pos

    def get_position(self):
        return self.position
