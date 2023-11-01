from pico2d import load_image, clear_canvas, update_canvas, get_events,SDL_KEYDOWN, SDLK_ESCAPE, SDL_QUIT, SDLK_SPACE

import game_world
import game_framework
import play_mode


def init():
    global image
    global x, y

    image = load_image('play.png')
    x, y = 400, 200


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image.draw(x, y, 435 / 3, 120 / 3)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)
