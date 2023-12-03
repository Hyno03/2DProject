from pico2d import *

import game_world
import game_framework
from countdown import Countdown
from floor import Floor
from item import Item, Obstacle
from npc import NPC
from player import Player
from swim_effect import Swim_Effect
from water import Water_Background, Line
import title_mode


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            for water_background in water_backgrounds:
                water_background.frames_per_action = 24
                water_background.time = get_time()
        else:
            player.handle_event(event)


def init():
    global countdown

    countdown = Countdown()
    game_world.add_object(countdown,3)

    background()
    swimmer()
    items()
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
    global water_backgrounds

    water_backgrounds = []
    positions = [500,310,130]
    for position in positions:
        water_background = Water_Background(position)
        game_world.add_object(water_background, 0)
        water_backgrounds.append(water_background)

    # floor
    front_floor = Floor(200, 20)
    game_world.add_object(front_floor, 3)

    #line
    line1 = Line(257)
    game_world.add_object(line1, 1)
    line2 = Line(437)
    game_world.add_object(line2, 1)


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
