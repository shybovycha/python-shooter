from cocos.particle import ParticleSystem, Color
from cocos.euclid import Point2
from src.core.modules.destroyable_particle_system import DestroyableParticleSystem

class PlasmaBall(DestroyableParticleSystem):
    """
        Pretty plasma missle particle system.
    """

    # total particles
    total_particles = 550

    # duration
    duration = -1

    # gravity
    gravity = Point2(-200, 0)

    # angle
    angle = 00.0
    angle_var = 0.0

    # speed of particles
    speed = 15.0
    speed_var = 5.0

    # radial
    radial_accel = 0
    radial_accel_var = 0

    # tangential
    tangential_accel = 0.0
    tangential_accel_var = 0.0

    # emitter variable position
    pos_var = Point2(0, 0)

    # life of particles
    life = 0.1
    life_var = 1.0

    # size, in pixels
    size = 10.0
    size_var = 10.0

    # emits per frame
    emission_rate = total_particles / life

    # color of particles
    start_color = Color(0.2, 0.7, 0.7, 1.0)
    start_color_var = Color(0.0, 0.0, 0.0, 0.2)
    end_color = Color(0.0, 0.0, 0.0, 1.0)
    end_color_var = Color(0.0, 0.0, 0.0, 0.0)

    # blend additive
    blend_additive = True

    # color modulate
    color_modulate = True

    def __init__(self, color = Color(0.2, 0.7, 0.7, 1.0)):
        super(PlasmaBall, self).__init__(self.size)

        self.start_color = color