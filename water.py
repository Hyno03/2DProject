from pico2d import load_image, get_time

import game_framework

WATER_TIME_PER_ACTION = 0.1
WATER_ACTION_PER_TIME = 1.0 / WATER_TIME_PER_ACTION

class Water_Background:
    def __init__(self, y = 0):
        self.image = load_image('Sprite/Background/water.png')
        self.x, self.y = 500, y
        self.w, self.h = self.image.w, self.image.h
        self.left_screen = 600
        self.frames_per_action = 8
        self.time = get_time()

    def draw(self):
        self.image.draw(self.x, self.y, self.w*2, self.h*2)
        self.image.draw(self.x + 1200, self.y, self.w*2, self.h*2)

    def update(self):
        self.x -= WATER_ACTION_PER_TIME * self.frames_per_action * game_framework.frame_time
        if self.x < -self.left_screen:
            self.x = self.left_screen
        if get_time() - self.time > 1:
            self.frames_per_action = 8

class Line:
    def __init__(self, y = 0):
        self.image = load_image('Sprite/Background/line.png')
        self.x, self.y = 100, y
        self.w, self.h = self.image.w, self.image.h

    def draw(self):
        self.image.draw(self.x, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 220, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 450, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 650, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 800, self.y, self.w * 4, self.h * 4)

    def update(self):
        pass
