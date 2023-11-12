from pico2d import load_image

class Floor:
    def __init__(self, x = 0 , y = 0):
        self.image = load_image('Sprite/Background/floor.png')
        self.x, self.y = x,y

    def draw(self):
        self.image.draw(self.x, self.y, 400, 100)
        self.image.draw(self.x + 400, self.y, 400, 100)


    def update(self):
        pass
