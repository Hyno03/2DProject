from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_UP, SDLK_DOWN, SDLK_LEFT, SDLK_RIGHT, SDLK_SPACE, \
    draw_rectangle

import game_framework
from swim_effect import Swim_Effect
from water import Water_Background


def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


def leftkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def leftkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def rightkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def rightkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def spacekey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def start_swimming(e):
    return e[0] == 'Start_Swim'


# Player Run Speed
PIXEL_PER_METER = (15.0 / 0.01)  # 15 pixel 1 cm
SWIM_SPEED_KMPH = 30.0  # Km / Hour
SWIM_SPEED_MPM = (SWIM_SPEED_KMPH * 1000.0 / 60.0)
SWIM_SPEED_MPS = (SWIM_SPEED_MPM / 60.0)
SWIM_SPEED_PPS = (SWIM_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
PLAYER_TIME_PER_ACTION = 0.5
PLAYER_ACTION_PER_TIME = 1.0 / PLAYER_TIME_PER_ACTION
PLAYER_FRAMES_PER_ACTION = 4


class Idle:
    @staticmethod
    def enter(player, e):
        player.dir = 0
        player.frame = 0
        player.ready_to_swim = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + PLAYER_FRAMES_PER_ACTION * PLAYER_ACTION_PER_TIME * game_framework.frame_time) % 3
        if get_time() - player.ready_to_swim > 3:
            player.statemachine.handle_event(('Start_Swim', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, int(player.frame) * player.height, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class Swim:
    @staticmethod
    def enter(player, e):
        if upkey_down(e) or downkey_up(e):
            player.dir = 1
            player.is_move_once = True
        elif upkey_up(e) or downkey_down(e):
            player.dir = -1
            player.is_move_once = True

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + PLAYER_FRAMES_PER_ACTION * PLAYER_ACTION_PER_TIME * game_framework.frame_time) % 4
        if player.is_move_once:
            player.y += player.dir * SWIM_SPEED_PPS * game_framework.frame_time
            player.is_move_once = False
        if player.y < 90 or player.y > 250:
            player.y -= player.dir * SWIM_SPEED_PPS * game_framework.frame_time
        player.swim_effect.update(player.x - 20, player.y + 90)

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, int(player.frame) * player.height + 72, player.width, player.height, player.x,
                               player.y,
                               player.width * 4, player.height * 4)
        player.swim_effect.draw()

#
# class Swim_Fast:
#     @staticmethod
#     def enter(player, e):
#         pass
#
#     @staticmethod
#     def exit(player, e):
#         pass
#
#     @staticmethod
#     def do(player):
#         player.frame = (player.frame + PLAYER_FRAMES_PER_ACTION * PLAYER_ACTION_PER_TIME * game_framework.frame_time) % 4
#         player.swim_effect.update(player.x - 20, player.y + 90)
#         player.water_background.action_per_time -= 0.01
#
#         player.water_background.update()
#
#     @staticmethod
#     def draw(player):
#         player.image.clip_draw(0, int(player.frame) * player.height + 72, player.width, player.height, player.x,
#                                player.y,
#                                player.width * 4, player.height * 4)
#         player.swim_effect.draw()
#         player.water_background.draw()


class AutoSwim:
    @staticmethod
    def enter(player, e):
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + PLAYER_FRAMES_PER_ACTION * PLAYER_ACTION_PER_TIME * game_framework.frame_time) % 4
        player.swim_effect.update(player.x - 20, player.y + 90)

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, int(player.frame) * player.height + 72, player.width, player.height, player.x,
                               player.y,
                               player.width * 4, player.height * 4)
        player.swim_effect.draw()


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transitions = {
            Idle: {start_swimming: AutoSwim},
            Swim: {upkey_up: AutoSwim, downkey_up: AutoSwim},
            AutoSwim: {upkey_down: Swim, downkey_down: Swim}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True
        return False


    def draw(self):
        self.cur_state.draw(self.player)


class Player:
    def __init__(self):
        self.image = load_image('Sprite/Player/redplayeranimation.png')
        self.x, self.y = 510, 150
        self.width, self.height = 24, 24
        self.frame = 0
        self.dir = 0
        self.statemachine = StateMachine(self)
        self.statemachine.start()
        self.swim_effect = Swim_Effect(self.x - 20, self.y + 90)
        self.item_gauge = 0
        self.is_move_once = False
        self.water_background = Water_Background(130)

    def handle_event(self, event):
        self.statemachine.handle_event(('INPUT', event))

    def draw(self):
        self.statemachine.draw()
        draw_rectangle(*self.get_bb())

    def update(self):
        self.statemachine.update()
        print(self.item_gauge)


    def get_bb(self):
        if self.statemachine.cur_state == Idle:
            return self.x - 25, self.y - 50, self.x + 25, self.y + 50
        else:
            return self.x - 30, self.y - 20, self.x + 30, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:item':
            self.item_gauge += 1
        if group == 'player:box':
            pass
