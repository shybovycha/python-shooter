from src.core.modules.destroyable_entity import DestroyableEntity
from src.core.modules.collidable_sprite import CollidableSprite

class DestroyableSprite(CollidableSprite, DestroyableEntity):
    """
        Represents sprite, which may both give and take damage when hit.
        This one may die.
    """

    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        CollidableSprite.__init__(self, image_path, position, rotation, bound_to_window)
        DestroyableEntity.__init__(self, self.radius)
