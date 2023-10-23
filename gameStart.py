from pico2d import load_image

import game_world


class GameStart:
    def __init__(self):
        self.image = load_image('play.png')
        self.x, self.y = 400, 200
        self.clicked = False

    def draw(self):
        self.image.draw(self.x, self.y, 435/3, 120/3)

    def update(self):
        if self.clicked:
            game_world.remove_object(self)
