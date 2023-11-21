from pico2d import load_image

import game_framework

# Water Action Speed
TIME_PER_ACTION = 0.1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Water:
    def __init__(self, x = 0, y = 0):
        self.image = load_image('Sprite/Background/wave.png')
        self.x, self.y = x, y
        self.left_screen = 200

    def draw(self):
        self.image.draw(self.x, self.y, 400, 80)
        self.image.draw(self.x + 400, self.y, 400, 80)
        self.image.draw(self.x + 800, self.y, 400, 80)
        self.image.draw(self.x + 1200, self.y, 400, 80)
        pass

    def update(self):
        self.x -= ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time
        if self.x < -self.left_screen:
            self.x = self.left_screen

class Water_Background:
    def __init__(self, y = 0):
        self.image = load_image('Sprite/Background/water.png')
        self.x, self.y = 500, y
        self.w, self.h = 640, 128
        self.left_screen = 600

    def draw(self):
        self.image.draw(self.x, self.y, self.w*2, self.h*2)
        self.image.draw(self.x + 1200, self.y, self.w*2, self.h*2)

    def update(self):
        self.x -= ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time
        if self.x < -self.left_screen:
            self.x = self.left_screen
