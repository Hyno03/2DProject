from pico2d import *

import game_world
import game_framework
from floor import Floor
from item import Item
from npc import NPC
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
    global npc1
    global item

    player = Player()
    game_world.add_object(player, 7)

    npc1 = NPC(300)
    game_world.add_object(npc1, 4)

    npc2 = NPC(420)
    game_world.add_object(npc2, 1)

    item = Item()
    game_world.add_object(item,7)

    background()


def background():
    global front_floor, back_floor
    global first_rail_front_water, first_rail_back_water
    global second_rail_front_water, second_rail_back_water
    global third_rail_front_water, third_rail_back_water

    # first rail
    first_rail_front_water = Water(0, 120)
    game_world.add_object(first_rail_front_water, 8)
    first_rail_back_water = Water(50, 180)
    game_world.add_object(first_rail_back_water, 6)
    # floor
    front_floor = Floor(200, 50)
    game_world.add_object(front_floor, 8)
    back_floor = Floor(200, 500)
    game_world.add_object(back_floor, 0)
    # second rail
    second_rail_front_water = Water(0, 240)
    game_world.add_object(second_rail_front_water, 5)
    second_rail_back_water = Water(50, 300)
    game_world.add_object(second_rail_back_water, 3)
    # third_rail
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
