import sys
import renderer, player
import ctypes
import sdl2, sdl2.ext

def run():
    sdl2.ext.init()

    window = sdl2.ext.Window("SlideShooter", size = (800, 600))

    window.show()

    world = sdl2.ext.World()

    sprite_renderer = renderer.SoftwareRenderer(window)
    world.add_system(sprite_renderer)

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

    player_sprite = sprite_factory.from_color(sdl2.ext.Color(140, 60, 60), size = (50, 50))

    player1 = player.Player(world, player_sprite, 200)

    running = True

    while running:
        events = sdl2.ext.get_events()

        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

        x, y = ctypes.c_int(0), ctypes.c_int(0)
        mouse_state = sdl2.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
        x, y = x.value, y.value
        w, h = window.size

        player1.set_position(min(h - player1.size[1], max(y, 0)))

        world.process()

if __name__ == "__main__":
    sys.exit(run())
