from pico2d import load_image

import game_world


class PlayButton:
    def __init__(self):
        self.image = load_image('Sprite/UI/play.png')
        self.x, self.y = 400, 200
        self.w, self.h = 435 / 3, 120 / 3
        self.clicked = False

    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)

    def update(self):
        if self.clicked == True:
            game_world.remove_object(self)
