from pico2d import *

import character_select_mode
import describe_mode
import end_mode
import game_world
import game_framework
import title_mode
from countdown import Countdown
from floor import Floor
from item import Item, Obstacle
from npc import NPC
from player import Player
from water import Water_Background, Line, Finish_Line


def handle_events():
    global finish_line
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(describe_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if player.item_gauge >= 5:
                for water_background in water_backgrounds:
                    water_background.frames_per_action = 24
                    water_background.time = get_time()
                player.item_gauge = 0
                player.swim_effect.frames_per_action = 8
                player.dir = 1
                player.swim_effect.time = get_time()
        elif all(finish_line.is_swim_finish.values()):
            game_framework.change_mode(end_mode)
            end_mode.winner = finish_line.the_winner
        else:
            player.handle_event(event)


def init():
    global countdown
    global finish_line

    countdown = Countdown()
    game_world.add_object(countdown, 3)

    background()
    items()
    swimmer()
    collide()

    time = get_time()
    finish_line = Finish_Line()
    if get_time() - time > 30:
        game_world.add_object(finish_line, 1)


def collide():
    global player
    global item
    global box
    global npc1
    global npc2

    game_world.add_collision_pair('player:item', player, None)
    game_world.add_collision_pair('player:box', player, None)
    game_world.add_collision_pair('player:end', player, None)
    game_world.add_collision_pair('npc:end', None, None)
    game_world.add_collision_pair('end:box', None, None)
    game_world.add_collision_pair('end:item', None, None)



def items():
    global item
    global box
    item = Item()
    game_world.add_object(item, 2)
    box = Obstacle()
    game_world.add_object(box, 2)


def swimmer():
    global player
    global npc1
    global npc2

    player = Player()
    game_world.add_object(player, 2)

    npc1 = NPC(100, 350)
    game_world.add_object(npc1, 2)

    npc2 = NPC(100, 520)
    game_world.add_object(npc2, 2)


def background():
    global water_backgrounds

    water_backgrounds = []
    positions = [500,310,130]
    for position in positions:
        water_background = Water_Background(position)
        game_world.add_object(water_background, 0)
        water_backgrounds.append(water_background)

    # floor
    front_floor = Floor(200, 20)
    game_world.add_object(front_floor, 2)

    #line
    line1 = Line(257)
    game_world.add_object(line1, 1)
    line2 = Line(437)
    game_world.add_object(line2, 1)


def finish():
    game_world.clear()


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
