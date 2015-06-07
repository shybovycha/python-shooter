import cocos

from cocos.text import Label

class StatusBarLayer(cocos.layer.Layer):
    """
        Layer, displaying player status.
    """

    is_event_handler = True

    def __init__(self, player, waves_cnt=0):
        super(StatusBarLayer, self).__init__()

        self.health_label = Label("", position=(10, 10), font_size=10)
        self.armor_label = Label("", position=(100, 10), font_size=10)
        self.wave_label = Label("", position=(200, 10), font_size=10)

        self.add(self.wave_label)
        self.add(self.armor_label)
        self.add(self.health_label)

        self.set_wave(0, waves_cnt)
        self.set_player_state(player)

    def set_wave(self, wave, waves_cnt):
        wave_str = "WAVE {0}/{1}".format(wave, waves_cnt)
        self.wave_label.element.text = wave_str

    def set_player_state(self, player):
        health_str = "HP {0}/{1}".format(player.health, player.max_health)
        self.health_label.element.text = health_str

        if player.armor is not None:
            health_str = "ARMOR {0}/{1}".format(player.armor.health, player.armor.max_health)
            self.health_label.element.text = health_str