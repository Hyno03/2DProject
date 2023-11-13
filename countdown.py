from pico2d import get_time, load_image

import game_world


class Countdown:
    def __init__(self):
        self.image1 = load_image('Sprite/UI/1.png')
        self.image2 = load_image('Sprite/UI/2.png')
        self.image3 = load_image('Sprite/UI/3.png')
        self.x, self.y = 500, 300
        self.w, self.h = 32, 36
        self.time = get_time()

    def draw(self):
        if 0 < get_time() - self.time < 1:
            self.image3.draw(self.x, self.y, self.w * 5, self.h * 5)
        if 1< get_time() - self.time < 2:
            self.image2.draw(self.x, self.y, self.w * 5, self.h * 5)
        if 2 < get_time() - self.time < 3:
            self.image1.draw(self.x, self.y, self.w * 5, self.h * 5)

    def update(self):
        if get_time() - self.time > 3:
            game_world.remove_object(self)
