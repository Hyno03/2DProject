from pico2d import load_image


class Floor:
    def __init__(self, x = 0 , y = 0):
        self.image = load_image('Sprite/Background/floor.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y, 400, 100)
        self.image.draw(self.x + 400, self.y, 400, 100)
        self.image.draw(self.x + 800, self.y, 400, 100)

    def update(self):
        pass


class Blue_Floor:
    def __init__(self):
        self.image = load_image('Sprite/Background/background.png')
        self.x, self.y = 500, 300
        self.w, self.h = self.image.w, self.image.h

    def draw(self):
        self.image.draw(self.x, self.y, self.w * 5, self.h * 5)

    def update(self):
        pass
