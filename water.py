from pico2d import load_image


class Water:
    def __init__(self,y = 0):
        self.image = load_image('wave.png')
        self.y = y

    def draw(self):
        self.image.draw(200, self.y, 400, 100)
        self.image.draw(600, self.y, 400, 100)
        pass

    def update(self):
        pass
