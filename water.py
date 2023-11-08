from pico2d import load_image


class Water:
    def __init__(self,y = 0):
        self.image = load_image('water.png')
        self.y = y

    def draw(self):
        self.image.draw(400, self.y, 800, 200)
        pass

    def update(self):
        pass
