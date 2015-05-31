from cocos.particle import ParticleSystem, Color
from cocos.euclid import Point2

class SpaceExplosion(ParticleSystem):
    """
        Class representing such a particle system, which simulates
        the explosion in a space
    """

    def rgb2color(r, g, b, a = 255.0):
        """
            Utilizes some helper methods for particle systems.
        """

        return Color(r / 255.0, g / 255.0, b / 255.0, a / 255.0)

    # total particle
    total_particles = 700

    # duration
    duration = 0.1

    # gravity
    gravity = Point2(0, 0)

    # angle
    angle = 90.0
    angle_var = 360.0

    # radial
    radial_accel = 0
    radial_accel_var = 0

    # speed of particles
    speed = 70.0
    speed_var = 80.0

    # emitter variable position
    pos_var = Point2(0, 0)

    # life of particles
    life = 0.5
    life_var = 0.2

    # emits per frame
    emission_rate = total_particles / duration

    # color of particles
    start_color = rgb2color(255, 250, 0)
    end_color = rgb2color(230, 0, 0)
    start_color_var = Color(0.8, 0.8, 0.8, 0.0)
    end_color_var = Color(0.2, 0.2, 0.2, 0.2)

    # size, in pixels
    size = 5.0
    size_var = 3.0

    # blend additive
    blend_additive = False

    # color modulate
    color_modulate = True

    def __init__(self):
        super(SpaceExplosion, self).__init__(self.size)
