from pico2d import load_image, clear_canvas, update_canvas, get_events, SDL_KEYDOWN, SDLK_ESCAPE, SDL_QUIT, SDLK_SPACE

import character_select_mode
import game_world
import game_framework
import play_mode
from title_page import Title_Page


def init():
    title_page = Title_Page()
    game_world.add_object(title_page, 0)


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(character_select_mode)
