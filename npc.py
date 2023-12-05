import random

from pico2d import load_image, get_time, draw_rectangle, clamp

import game_framework
import game_world
from behavior_tree import BehaviorTree
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
        npc.x += npc.dir * npc.speed * game_framework.frame_time
        npc.x = clamp(100, npc.x, 900)
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
    def __init__(self, x, y):
        self.image = load_image('Sprite/Player/blackplayeranimation.png')
        self.x, self.y = x, y
        self.width, self.height = 24, 24
        self.frame = 0
        self.dir = 1
        self.statemachine = StateMachine(self)
        self.statemachine.start()
        self.swim_effect = Swim_Effect(self.x - 20, self.y + 90)
        self.speed = SWIM_SPEED_PPS
        self.dir_rand = [1, -1]
        self.rand_time, self.time = get_time(), get_time()
        self.random_value = 1
        game_world.add_collision_pair('npc:end', self, None)



    def handle_event(self, event):
        self.statemachine.handle_event(('INPUT', event))

    def draw(self):
        self.statemachine.draw()
        # draw_rectangle(*self.get_bb())

    def update(self):
        if get_time() - self.rand_time > 2 and get_time() - self.time < 30:
            self.dir = random.choice(self.dir_rand)
            self.random_value = random.randint(5, 10)
            self.rand_time = get_time()
        if get_time() - self.time > 30:
            self.dir = 1
            self.random_value = 5
        self.speed = SWIM_SPEED_PPS / self.random_value
        self.statemachine.update()

    def get_bb(self):
        if self.statemachine.cur_state == Idle:
            return self.x - 25, self.y - 50, self.x + 25, self.y + 50
        else:
            return self.x - 30, self.y - 20, self.x + 30, self.y + 20

    def handle_collision(self, group, other):
        if group == 'npc:end':
            self.statemachine.cur_state = Idle