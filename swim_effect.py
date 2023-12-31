from pico2d import load_image, get_time

import game_framework
from water import Water_Background

# Water Action Speed
TIME_PER_ACTION = 0.1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

class Swim_Effect:
    def __init__(self, x = 0, y = 0):
        self.image = load_image('Sprite/Background/3.png')
        self.x, self.y = x, y
        self.w, self.h = 48, 48
        self.frame = 0
        self.frames_per_action = 1
        self.water = Water_Background()
        self.time = get_time()

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.w, 0, self.w, self.h, self.x, self.y, self.w * 5, self.h * 5)

    def update(self, x = 0, y = 0):
        self.x, self.y = x, y
        self.frame = (self.frame + self.frames_per_action * ACTION_PER_TIME * game_framework.frame_time) % 4
        if get_time() - self.time > 1:
            self.frames_per_action = 1