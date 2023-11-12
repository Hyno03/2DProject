from pico2d import *

import game_world
import game_framework
from player import Player
import title_mode
from water import Water


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            player.handle_event(event)


def init():
    global player
    global first_rail_front_water, first_rail_back_water
    global second_rail_front_water, second_rail_back_water
    global third_rail_front_water, third_rail_back_water

    player = Player()
    game_world.add_object(player, 7)

    #first rail
    first_rail_front_water = Water(0,120)
    game_world.add_object(first_rail_front_water, 8)

    first_rail_back_water = Water(50,180)
    game_world.add_object(first_rail_back_water, 6)

    #second rail
    second_rail_front_water = Water(0, 240)
    game_world.add_object(second_rail_front_water, 5)

    second_rail_back_water = Water(50, 300)
    game_world.add_object(second_rail_back_water, 3)

    #third_rail
    second_rail_front_water = Water(0, 360)
    game_world.add_object(second_rail_front_water, 2)

    second_rail_back_water = Water(50, 420)
    game_world.add_object(second_rail_back_water, 0)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
