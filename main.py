from pico2d import *

import game_world
from gameStart import GameStart


def handle_events():
    global mouse_x, mouse_y
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     mouse_x, mouse_y = event.x, 600 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                gameStart.clicked = True


def reset_world():
    global mouse_x, mouse_y
    global running
    global gameStart

    running = True

    gameStart = GameStart()
    game_world.add_object(gameStart, 0)

    mouse_x, mouse_y = 0, 0


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
close_canvas()
