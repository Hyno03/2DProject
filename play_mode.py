from pico2d import *

import game_world
import game_framework
from countdown import Countdown
from floor import Floor
from item import Item, Obstacle
from npc import NPC
from player import Player
from water import Water, Water_Background
import title_mode


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
    global countdown

    countdown = Countdown()
    game_world.add_object(countdown,3)

    swimmer()
    items()
    background()
    collide()


def collide():
    global player
    global item
    global box

    game_world.add_collision_pair('player:item', player, None)
    game_world.add_collision_pair('player:box', player, None)


def items():
    global item
    global box
    item = Item()
    game_world.add_object(item, 1)
    box = Obstacle()
    game_world.add_object(box, 1)


def swimmer():
    global player
    global npc1

    player = Player()
    game_world.add_object(player, 1)

    npc1 = NPC(320)
    game_world.add_object(npc1, 1)

    npc2 = NPC(490)
    game_world.add_object(npc2, 1)


def background():
    #background water
    water_background = Water_Background()
    game_world.add_object(water_background, 0)

    # first rail
    first_rail_water = Water(0, 100)
    game_world.add_object(first_rail_water, 2)

    # second rail
    second_rail_water = Water(0, 270)
    game_world.add_object(second_rail_water, 2)

    # third_rail
    second_rail_water = Water(0, 440)
    game_world.add_object(second_rail_water, 2)

    # floor
    front_floor = Floor(200, 20)
    game_world.add_object(front_floor, 0)
    back_floor = Floor(200, 600)
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
