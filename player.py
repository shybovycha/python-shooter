import sys, sdl2, sdl2.ext

class Player(sdl2.ext.Entity):
    x_padding = 20
    
    def __init__(self, world, sprite, y = 0):
        self.sprite = sprite
        self.sprite.position = self.x_padding, y

    def set_position(self, y):
        self.sprite.position = self.x_padding, y

    @property
    def size(self):
        return self.sprite.size

