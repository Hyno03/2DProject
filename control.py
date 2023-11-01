from pico2d import *

import game_world
from player import Player
# from title_mode import GameStart


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # elif event.type == SDL_MOUSEBUTTONDOWN:
        #     if event.button == SDL_BUTTON_LEFT:
        #         mouse_x, mouse_y = event.x, 600 - event.y
        #         # 스타트 버튼 누를 시 사라짐
        #         if gameStart.x - gameStart.image.w // 2 < mouse_x < gameStart.x + gameStart.image.w // 2 and \
        #                 gameStart.y - gameStart.image.h // 2 < mouse_y < gameStart.y + gameStart.image.h // 2:
        #             gameStart.clicked = True


def reset_world():
    global running
    global gameStart
    global player

    running = True
    #
    # gameStart = GameStart()
    # # game_world.add_object(gameStart, 0)

    player = Player()
    # if gameStart.clicked:
    game_world.add_object(player, 0)


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.1)
close_canvas()
