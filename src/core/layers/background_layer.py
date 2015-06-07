import cocos

from src.core.modules.parallax_layer import ParallaxLayer
from src.core.modules.resource_manager import ResourceManager

class BackgroundLayer(cocos.layer.Layer):
    """
        Parallax background
    """

    is_event_handler = True

    def __init__(self, image=None):
        super(BackgroundLayer, self).__init__()

        if image is None:
            image = ResourceManager.get_background_image()

        self.parallax_layer = ParallaxLayer(image)

        self.add(self.parallax_layer.bg_img1.sprite)
        self.add(self.parallax_layer.bg_img2.sprite)

    def _step(self, delta_time):
        """
            Handle parallax effect each timer tick
        """

        self.parallax_layer.shift_background(delta_time)
