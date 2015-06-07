from pyglet.event import EventDispatcher

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.shooting_sprite import ShootingSprite
from src.core.modules.missle import Missle
from src.core.modules.enemy import Enemy

class Player(ShootingSprite, EventDispatcher):
    """
        Represents player, the Space Hero.
    """

    SERIALIZABLE_PARAMS = ['health', 'max_health', 'armor', 'missle_damage', 'score']

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

    def get_params(self):
        """
            Returns params needed for restore
        """

        return {key: getattr(self, key) for key in Player.SERIALIZABLE_PARAMS}

    def set_params(self, params):
        """
            Restores params
        """

        for key, value in params.items():
            if not key in Player.SERIALIZABLE_PARAMS:
                continue

            setattr(self, key, value)

    def on_hit_entity(self, entity):
        """
            Player hits entity. Handler.

            * when entity is a missle - player takes damage
            * when entity is a bonus - player picks it up and bonus "dies"
            * when entity is an enemy - player takes huge damage; enemy too
        """

        self.dispatch_event('on_player_hit', self)

        if isinstance(entity, Enemy):
            self.take_damage(entity.hit_damage)

        if isinstance(entity, Missle) and not isinstance(entity.owner, Player):
            self.take_damage(entity.hit_damage)

    def gain_score_points(self, points_gained):
        """
            Points are gained for enemy kills and bonus pick-ups.
        """

        self.score += points_gained

Player.register_event_type('on_player_hit')
