from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

testinfo = "f 10 0.033, s, f 20 0.033, s, f 30 0.033, s, f 30 0.033, s, q"
tags = "particles, Explosion"

import pyglet
import cocos
from cocos.director import director
from cocos.actions import *
from cocos.layer import *
from cocos.particle_systems import *
from cocos.particle import ParticleSystem, Color
from cocos.euclid import Point2

class SpaceExplosion(ParticleSystem):
    def rgb2color(r, g, b, a = 255.0):
        return Color(r / 255.0, g / 255.0, b / 255.0, a / 255.0)

    # total particle
    total_particles = 1700

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

class PlasmaBall(ParticleSystem):

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

class L(Layer):
    def __init__(self):
        super( L, self).__init__()

        # p = Fireworks()
        # p = Explosion()
        # p = SpaceExplosion()
        # p = Fire()
        # p = Flower()
        # p = Sun()
        # p = Spiral()
        # p = Meteor()
        p = SpaceMeteor()
        # p = Galaxy()

        p.auto_remove_on_finish = True

        p.position = (320,240)
        self.add( p )

def main():
    director.init( resizable=True )
    main_scene = cocos.scene.Scene()

    main_scene.add( L() )

    director.run( main_scene )

if __name__ == '__main__':
    main()