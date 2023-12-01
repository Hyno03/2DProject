from pico2d import load_image, clear_canvas, update_canvas, get_events, SDL_KEYDOWN, SDLK_ESCAPE, SDL_QUIT, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT

import game_world
import game_framework
import play_mode
from floor import White_Floor
from play_button import PlayButton
from water import Water_Background


def init():
    global play_button

    play_button = PlayButton()
    game_world.add_object(play_button,1)

    gray_background()

    water = Water_Background(120)
    game_world.add_object(water, 0)


def gray_background():

    floor = White_Floor(0, 250)
    game_world.add_object(floor, 0)
    floor = White_Floor(0, 350)
    game_world.add_object(floor, 0)
    floor = White_Floor(0, 450)
    game_world.add_object(floor, 0)
    floor = White_Floor(0, 550)
    game_world.add_object(floor, 0)


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
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mouse_x, mouse_y = event.x, 600 - event.y
                if play_button.x - play_button.image.w // 2 < mouse_x < play_button.x + play_button.image.w // 2 and \
                        play_button.y - play_button.image.h // 2 < mouse_y < play_button.y + play_button.image.h // 2:
                    play_button.clicked = True
                    game_framework.change_mode(play_mode)
