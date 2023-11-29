from pico2d import *

import game_world
import game_framework
from countdown import Countdown
from floor import Floor
from item import Item, Obstacle
from npc import NPC
from player import Player
from water import Water_Background
import title_mode


def handle_events():
    global running
    global swim_fast_time

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(title_mode)
            elif event.key == (SDLK_LEFT or SDLK_RIGHT):
                water_background1.action_per_time += 1
                swim_fast_time = get_time()
        elif event.type == SDL_KEYUP:
            if event.key == (SDLK_LEFT or SDLK_RIGHT) and get_time() - swim_fast_time > 1:
                water_background1.action_per_time = 8
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

    npc1 = NPC(350)
    game_world.add_object(npc1, 1)

    npc2 = NPC(520)
    game_world.add_object(npc2, 1)


def background():
    global water_background1
    #background water 1
    water_background1 = Water_Background(500)
    game_world.add_object(water_background1, 0)


    #background water 2
    water_background2 = Water_Background(310)
    game_world.add_object(water_background2, 0)

    #
    #background water 3
    water_background3 = Water_Background(130)
    game_world.add_object(water_background3, 0)

    # floor
    front_floor = Floor(200, 20)
    game_world.add_object(front_floor, 0)
    # back_floor = Floor(200, 650)
    # game_world.add_object(back_floor, 0)


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
