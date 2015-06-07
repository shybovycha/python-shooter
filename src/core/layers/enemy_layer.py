import cocos

from pyglet.event import EventDispatcher

from cocos.actions import ScaleTo, FadeIn, FadeOut, Delay, CallFunc
from cocos.layer.base_layers import Layer

from src.core.modules.sprite import Sprite
from src.core.modules.collision_manager import CollisionManager

import src.core.modules.game_manager

class EnemyLayer(Layer, EventDispatcher):
    """
        Layer, containing and controlling enemies.
    """

    is_event_handler = True

    def __init__(self):
        Layer.__init__(self)
        EventDispatcher.__init__(self)

        self.waves = []
        self.current_wave = None
        self.wave_delay = 3
        self.countdown_label = None
        self.countdown_texts = []
        self.is_started = False
        self.is_next_wave_notified = False
        self.is_enemies_deployed = False
        self.next_level_notified = False
        self.bonuses = []

    def generate_countdown_texts(self):
        """
            Generates set of labels for countdown timer
        """

        numbers = [str(i) for i in reversed(range(1, self.wave_delay + 1))]
        self.countdown_texts = ["Get ready!"]
        self.countdown_texts.extend(numbers)
        self.countdown_texts.append("Let's rock!")

    def set_enemy_waves(self, waves):
        """
            Sets enemy waves
        """

        self.waves = waves

    def has_enemies(self):
        """
            Checks if there are any alive enemies on the scene.
        """

        return len(self.alive_enemies()) > 0

    def alive_enemies(self):
        """
            Returns a list of alive enemies on the scene. Used for update.
        """

        return [enemy for enemy in self.enemies() if enemy.is_alive()]

    def enemies(self):
        """
            Returns enemies from the current wave.
        """

        if (self.current_wave is None) or (self.is_done()):
            return []
        else:
            return self.waves[self.current_wave]

    def missles(self):
        """
            Returns all the missles alive for all the enemies alive.
        """

        result = sum([enemy.missles for enemy in self.enemies()], [])
        return [missle for missle in result if missle.is_alive()]

    def register_bonus(self, bonus):
        """
            Tracks single bonus dropped
        """

        self.add(bonus.sprite)
        self.bonuses.append(bonus)
        CollisionManager.register(bonus)

    def is_done(self):
        """
            Checks if this level is done.
        """

        return self.current_wave is not None and self.current_wave >= len(self.waves)

    def deploy_enemies(self):
        """
            Creates sprites of all the enemies in the current wave
        """

        if self.current_wave is None:
            self.current_wave = 0
        else:
            self.current_wave += 1

        for enemy in self.enemies():
            self.add(enemy.sprite)

            CollisionManager.register(enemy)

        self.is_enemies_deployed = True
        self.dispatch_event('on_next_wave', self.current_wave + 1, len(self.waves))

    def update_countdown_label(self):
        """
            This huge method just creates a label like "Get ready! 5 4 3 2 1 GO!"
        """

        if len(self.countdown_texts) < 1:
            self.countdown_label = None
            self.deploy_enemies()
            self.is_next_wave_notified = False
            self.is_started = True
            return

        text = self.countdown_texts.pop(0)

        if self.countdown_label is None:
            font_size = 32
            half_label_size = font_size / 2
            screen_width, screen_height = Sprite.window_size()
            screen_center_x = (screen_width / 2) - half_label_size
            screen_center_y = (screen_height / 2) - half_label_size
            screen_center = (screen_center_x, screen_center_y)

            self.countdown_label = cocos.text.Label(text,
                                                    font_size=font_size,
                                                    anchor_x='center',
                                                    anchor_y='center')

            self.countdown_label.position = screen_center
            self.add(self.countdown_label)

        self.countdown_label.element.text = text

        fade_in = FadeIn(0.1)
        scale1 = ScaleTo(3, duration=0.75)
        fade_out = Delay(0.75) + FadeOut(0.24)
        scale2 = Delay(0.99) + ScaleTo(1, duration=0.1)
        call_update = Delay(1.1) + CallFunc(self.update_countdown_label)
        label_animation = fade_in | scale1 | fade_out | scale2 | call_update

        self.countdown_label.do(label_animation)

    def next_wave(self):
        """
            Starts the countdown and then deploys new wave.
        """

        self.generate_countdown_texts()
        self.update_countdown_label()

    def _step(self, delta_time):
        """
            Called each frame. This is a good place to
            update all enemies and their missles.
        """

        if self.is_started and self.is_enemies_deployed and not self.has_enemies():
            if self.current_wave >= len(self.waves) - 1 and not self.next_level_notified:
                self.next_level_notified = True
                next_level_func = src.core.modules.game_manager.GameManager.next_level
                goto_next_level = Delay(2) + CallFunc(next_level_func)
                self.parent.do(goto_next_level)
            else:
                if not self.is_next_wave_notified:
                    self.is_enemies_deployed = False
                    self.is_next_wave_notified = True

                    deploy_next_wave = Delay(2) + CallFunc(self.next_wave)
                    self.parent.do(deploy_next_wave)

        CollisionManager.update()

        _enemies = self.alive_enemies()
        _missles = self.missles()

        screen_width, _ = Sprite.window_size()

        for enemy in _enemies:
            enemy.update(delta_time)

        for missle in _missles:
            missle.update(delta_time)

            if missle.get_x() < 0 or missle.get_x() > screen_width:
                missle.die()

        for bonus in self.bonuses:
            bonus.update(delta_time)

            if bonus.get_x() < 0 or bonus.get_x() > screen_width:
                bonus.die()

EnemyLayer.register_event_type('on_next_wave')
