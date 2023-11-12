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
        self.image.draw(self.x, self.y, 400, 100)
        self.image.draw(self.x + 400, self.y, 400, 100)
        self.image.draw(self.x + 800, self.y, 400, 100)
        pass

    def update(self):
        self.x -= ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time
        if self.x < -self.left_screen:
            self.x = self.left_screen
