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
    global firstrail_frontwater
    global firstrail_backwater

    player = Player()
    game_world.add_object(player, 1)

    firstrail_frontwater = Water(120)
    game_world.add_object(firstrail_frontwater,2)

    firstrail_backwater = Water(180)
    game_world.add_object(firstrail_backwater,0)



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
