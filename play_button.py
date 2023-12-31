from pico2d import load_image, load_font

import game_world


class PlayButton:
    def __init__(self):
        self.image = load_image('Sprite/UI/play.png')
        self.x, self.y = 500, 150
        self.w, self.h = 435 / 3, 120 / 3
        self.clicked = False
        self.font = load_font('neodgm.ttf', 100)

    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)
        self.font.draw(190, self.y + 250, f'Swimming Game', (0, 0, 0))

    def update(self):
        if self.clicked == True:
            game_world.remove_object(self)
