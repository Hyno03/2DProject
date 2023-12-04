from pico2d import load_image, get_time

import game_framework
from swim_effect import Swim_Effect


def start_swimming(e):
    return e[0] == 'Start_Swim'


# NPC Run Speed
PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel 20 cm
SWIM_SPEED_KMPH = 30.0  # Km / Hour
SWIM_SPEED_MPM = (SWIM_SPEED_KMPH * 1000.0 / 60.0)
SWIM_SPEED_MPS = (SWIM_SPEED_MPM / 60.0)
SWIM_SPEED_PPS = (SWIM_SPEED_MPS * PIXEL_PER_METER)

# NPC Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Idle:
    @staticmethod
    def enter(npc, e):
        npc.dir = 0
        npc.frame = 0
        npc.ready_to_swim = get_time()

    @staticmethod
    def exit(npc, e):
        pass

    @staticmethod
    def do(npc):
        npc.frame = (npc.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if get_time() - npc.ready_to_swim > 3:
            npc.statemachine.handle_event(('Start_Swim', 0))

    @staticmethod
    def draw(npc):
        npc.image.clip_draw(0, int(npc.frame) * npc.height, npc.width, npc.height, npc.x, npc.y,
                               npc.width * 4, npc.height * 4)


class AutoSwim:
    @staticmethod
    def enter(npc, e):
        pass

    @staticmethod
    def exit(npc, e):
        pass

    @staticmethod
    def do(npc):
        npc.frame = (npc.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        npc.swim_effect.update(npc.x - 20, npc.y + 90)

    @staticmethod
    def draw(npc):
        npc.image.clip_draw(0, int(npc.frame) * npc.height + 72, npc.width, npc.height, npc.x,
                               npc.y,
                               npc.width * 4, npc.height * 4)
        npc.swim_effect.draw()

class StateMachine:
    def __init__(self, npc):
        self.npc = npc
        self.cur_state = Idle
        self.transitions = {
            Idle: {start_swimming: AutoSwim},
            AutoSwim: { }
        }

    def start(self):
        self.cur_state.enter(self.npc, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.npc)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.npc, e)
                self.cur_state = next_state
                self.cur_state.enter(self.npc, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.npc)


class NPC:
    def __init__(self, y):
        self.image = load_image('Sprite/Player/blackplayeranimation.png')
        self.x, self.y = 100, y
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

    def update(self):
        self.statemachine.update()
