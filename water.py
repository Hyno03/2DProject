from pico2d import load_image


class Water:
    def __init__(self, y = 0):
        self.image = load_image('Sprite/Background/wave.png')
        self.x, self.y = 200, y

    def draw(self):
        self.image.draw(self.x, self.y, 400, 100)
        self.image.draw(self.x + 400, self.y, 400, 100)
        pass

    def update(self):
        pass
