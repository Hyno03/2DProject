from pico2d import load_image

import game_framework


class Water_Background:
    def __init__(self, y = 0):
        self.image = load_image('Sprite/Background/water.png')
        self.x, self.y = 500, y
        self.w, self.h = self.image.w, self.image.h
        self.left_screen = 600
        self.time_per_action = 0.1
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = 8

    def draw(self):
        self.image.draw(self.x, self.y, self.w*2, self.h*2)
        self.image.draw(self.x + 1200, self.y, self.w*2, self.h*2)

    def update(self):
        self.x -= self.action_per_time * self.frames_per_action * game_framework.frame_time
        if self.x < -self.left_screen:
            self.x = self.left_screen
