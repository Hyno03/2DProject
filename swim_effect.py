from pico2d import load_image

import game_framework

# Water Action Speed
TIME_PER_ACTION = 0.1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1

class Swim_Effect:
    def __init__(self, x = 0 , y = 0):
        self.image = load_image('Sprite/Background/3.png')
        self.x, self.y = x, y
        self.w, self.h = 48, 48
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.w, 0, self.w, self.h, self.x, self.y, self.w * 5, self.h * 5)

    def update(self, x = 0, y = 0):
        self.x, self.y = x, y
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass