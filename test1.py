import cocos, pyglet

class App(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(App, self).__init__()

        self.label = cocos.text.Label('Hello, app!',
                                 font_name = 'Arial',
                                 font_size = 32,
                                 anchor_x = 'center',
                                 anchor_y = 'center')

        self.label.position = 320, 240
        self.add(self.label)

        self.keys_pressed = set()
        self.update_text()

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
        text = 'Keys:' + (', '.join(key_names))
        self.label.element.text = text

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()

if (__name__ == '__main__'):
    cocos.director.director.init()

    app = App()
    main_scene = cocos.scene.Scene(app)
    cocos.director.director.run(main_scene)
