from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_UP, SDLK_DOWN, SDLK_SPACE, draw_rectangle

import game_framework
from swim_effect import Swim_Effect


def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


def start_swimming(e):
    return e[0] == 'Start_Swim'


# Player Run Speed
PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel 20 cm
SWIM_SPEED_KMPH = 30.0  # Km / Hour
SWIM_SPEED_MPM = (SWIM_SPEED_KMPH * 1000.0 / 60.0)
SWIM_SPEED_MPS = (SWIM_SPEED_MPM / 60.0)
SWIM_SPEED_PPS = (SWIM_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


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
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
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
        elif upkey_up(e) or downkey_down(e):
            player.dir = -1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        player.y += player.dir * SWIM_SPEED_PPS * game_framework.frame_time
        # if player.y < 170 or player.y > 230:
        #     player.y -= player.dir * 15
        player.swim_effect.update(player.x - 20, player.y + 90)

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, int(player.frame) * player.height + 72, player.width, player.height, player.x,
                               player.y,
                               player.width * 4, player.height * 4)
        player.swim_effect.draw()


class AutoSwim:
    @staticmethod
    def enter(player, e):
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
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
        self.x, self.y = 400, 180
        self.width, self.height = 24, 24
        self.frame = 0
        self.dir = 0
        self.statemachine = StateMachine(self)
        self.statemachine.start()
        self.swim_effect = Swim_Effect(self.x - 20, self.y + 90)

    def handle_event(self, event):
        self.statemachine.handle_event(('INPUT', event))

    def draw(self):
        self.statemachine.draw()
        draw_rectangle(*self.get_bb())

    def update(self):
        self.statemachine.update()

    def get_bb(self):
        if self.statemachine.cur_state == Idle:
            return self.x - 25, self.y - 50, self.x + 25, self.y + 50
        else:
            return self.x - 30, self.y - 25, self.x + 30, self.y + 25

    def handle_collision(self, group, other):
        if group == 'player:item':
            pass
