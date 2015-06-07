from pyglet.event import EventDispatcher

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.shooting_sprite import ShootingSprite
from src.core.modules.missle import Missle
from src.core.modules.enemy import Enemy

class Player(ShootingSprite, EventDispatcher):
    """
        Represents player, the Space Hero.
    """

    def __init__(self, image=None):
        if image is None:
            image = ResourceManager.get_player_image()

        ShootingSprite.__init__(self, image, rotation=90, bound_to_window=True)
        EventDispatcher.__init__(self)

        self.health = 100
        self.max_health = 100
        self.armor = None
        self.missle_damage = 10
        self.hit_damage = 100
        self.score = 0
        self.detonate = True

    def on_hit_entity(self, entity):
        """
            Player hits entity. Handler.

            * when entity is a missle - player takes damage
            * when entity is a bonus - player picks it up and bonus "dies"
            * when entity is an enemy - player takes huge damage; enemy too

            TODO: implement bonus hits player
        """

        if isinstance(entity, Enemy):
           self.take_damage(entity.hit_damage)

        if isinstance(entity, Missle) and not isinstance(entity.owner, Player):
            self.take_damage(entity.hit_damage)

        self.dispatch_event('on_player_hit', self)

    def gain_score_points(self, points_gained):
        """
            Points are gained for enemy kills and bonus pick-ups.
        """

        self.score += points_gained

Player.register_event_type('on_player_hit')