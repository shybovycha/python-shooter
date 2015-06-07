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
        self.armor_label = Label("", position=(150, 10), font_size=10)
        self.wave_label = Label("", position=(300, 10), font_size=10)

        self.add(self.wave_label)
        self.add(self.armor_label)
        self.add(self.health_label)

        self.set_wave(0, waves_cnt)
        self.set_player_state(player)

    def set_wave(self, wave, waves_cnt):
        """
            Updates wave status bar item
        """

        wave_str = "WAVE {0}/{1}".format(wave, waves_cnt)
        self.wave_label.element.text = wave_str

    def set_player_state(self, player):
        """
            Updates player' health and armor status bar items
        """

        health_str = "HP {0}/{1}".format(int(player.health), int(player.max_health))
        self.health_label.element.text = health_str

        if player.armor is not None:
            armor_hp = int(player.armor.health)
            max_armor_hp = int(player.armor.max_health)
            armor_str = "ARMOR {0}/{1}".format(armor_hp, max_armor_hp)
            self.armor_label.element.text = armor_str
