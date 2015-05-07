import cocos

from src.core.modules.parallax_layer import ParallaxLayer

class BackgroundLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(BackgroundLayer, self).__init__()

        self.parallax_layer = ParallaxLayer('resources/backgrounds/space1.png')

        self.add(self.parallax_layer.bg_img1.sprite)
        self.add(self.parallax_layer.bg_img2.sprite)

    def _step(self, dt):
        self.parallax_layer.shift_background(dt)
