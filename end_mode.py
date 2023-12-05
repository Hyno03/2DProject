from pico2d import *

import game_framework
import game_world
import play_mode
import title_mode
from floor import Blue_Floor


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(title_mode)



def init():
    global winner
    winner = None



def finish():
    game_world.clear()


def update():

    global winner
    blue_floor = Blue_Floor(winner)
    game_world.add_object(blue_floor, 0)
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass