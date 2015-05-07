from src.modules.collidable_sprite import CollidableSprite

class Player(CollidableSprite):
    def __init__(self):
        player_img = 'resources/ships/spaceship1_final.png'
        super(Player, self).__init__(player_img, rotation=90, bound_to_window=True)
