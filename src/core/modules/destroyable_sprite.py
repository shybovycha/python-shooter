from src.core.modules.destroyable_entity import DestroyableEntity
from src.core.modules.collidable_sprite import CollidableSprite
from src.core.modules.space_explosion import SpaceExplosion

class DestroyableSprite(CollidableSprite, DestroyableEntity):
    """
        Represents sprite, which may both give and take damage when hit.
        This one may die.
    """

    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        CollidableSprite.__init__(self, image_path, position, rotation, bound_to_window)
        DestroyableEntity.__init__(self, self.radius)

    def die(self):
        """
            Extend default `die` method to remove the correct
            entity from a layer and create an awesome explosion FX!
        """


        layer = self.sprite.parent

        explosion = SpaceExplosion()
        explosion.position = self.position()
        layer.add(explosion)

        DestroyableEntity.die(self)
        self.sprite.kill()
