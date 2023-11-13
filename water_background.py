from pico2d import load_image


class Water_Background:
    def __init__(self):
        self.image = load_image('Sprite/Background/wave.png')
        self.x, self.y = 400, 265

    def draw(self):
        self.image.draw(self.x, self.y, 800, 1000)

    def update(self):
        pass
