from collidable_sprite import CollidableSprite

class Player(CollidableSprite):
    def __init__(self):
        super(Player, self).__init__('resources/ships/spaceship1_final.png', rotation = 90, bound_to_window = True)