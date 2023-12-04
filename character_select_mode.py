from pico2d import *

import game_framework
import game_world
import title_mode
import play_mode
from character_select_page import Character_Select, Select_Box
from floor import Blue_Floor


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)



def init():
    global select_box

    background = Blue_Floor()
    game_world.add_object(background, 0)

    select_box = Select_Box()
    game_world.add_object(select_box, 1)

    character_select = Character_Select()
    game_world.add_object(character_select, 1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def update():
    game_world.update()


def finish():
    game_world.clear()


def pause():
    pass


def resume():
    pass
