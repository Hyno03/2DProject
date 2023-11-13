from pico2d import *

import game_world
import game_framework
from floor import Floor
from item import Item
from npc import NPC
from player import Player
from swim_effect import Swim_Effect
from water import Water
import title_mode
from water_background import Water_Background


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
    game_world.add_object(item, 7)

    background()
    collide()


def collide():
    global player
    global item

    game_world.add_collision_pair('player:item', player, None)


def background():
    global front_floor, back_floor
    global first_rail_water
    global second_rail_water
    global third_rail_water

    # first rail
    first_rail_water = Water(0, 120)
    game_world.add_object(first_rail_water, 8)

    #background water
    water_background = Water_Background()
    game_world.add_object(water_background, 0)

    # second rail
    second_rail_water = Water(0, 240)
    game_world.add_object(second_rail_water, 5)

    # third_rail
    second_rail_water = Water(0, 360)
    game_world.add_object(second_rail_water, 2)

    # floor
    front_floor = Floor(200, 50)
    game_world.add_object(front_floor, 8)
    back_floor = Floor(200, 530)
    game_world.add_object(back_floor, 0)


def finish():
    game_world.clear()
    pass


def update():
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
