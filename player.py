from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_UP, SDLK_DOWN, SDLK_SPACE
import game_framework

def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


def spacekey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def spacekey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE

# Player Run Speed
PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel 20 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Idle:
    @staticmethod
    def enter(player, e):
        player.dir = 0
        player.frame = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

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
        player.y += player.dir * RUN_SPEED_PPS * game_framework.frame_time
        # if player.y < 170 or player.y > 230:
        #     player.y -= player.dir * 15

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, int(player.frame) * player.height + 72, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class AutoSwim:
    @staticmethod
    def enter(player, e):
        if spacekey_down(e):
            player.dir = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, int(player.frame) * player.height + 72, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transitions = {
            Idle: {spacekey_down: AutoSwim},
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
        self.x, self.y = 400, 200
        self.width, self.height = 24, 24
        self.frame = 0
        self.dir = 0
        self.statemachine = StateMachine(self)
        self.statemachine.start()

    def handle_event(self, event):
        self.statemachine.handle_event(('INPUT', event))

    def draw(self):
        self.statemachine.draw()

    def update(self):
        self.statemachine.update()
