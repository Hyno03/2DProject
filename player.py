from pico2d import load_image

import game_world


class Player:
    def __init__(self):
        self.image = load_image('redplayeranimation.png')
        self.x, self.y = 400, 200
        self.width, self.height = 24, 23
        self.frame = 0

    def draw(self):
        self.image.clip_draw(0, self.frame * self.height, self.width, self.height, self.x, self.y, self.width * 4,
                             self.height * 4)

    def update(self):
        self.frame = (self.frame + 1) % 4
