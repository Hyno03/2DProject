from pico2d import load_image


class Title_Page:
    def __init__(self):
        self.image = load_image('Sprite/Background/main_page.png')
        self.x, self.y = 500, 300

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
