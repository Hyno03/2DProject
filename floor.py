from pico2d import load_image, load_font



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
    def __init__(self, winner):
        self.image = load_image('Sprite/Background/background.png')
        self.x, self.y = 500, 300
        self.w, self.h = self.image.w, self.image.h
        self.font = load_font('neodgm.ttf', 100)
        self.font2 = load_font('neodgm.ttf', 30)
        self.the_winner = winner

    def draw(self):
        self.image.draw(self.x, self.y, self.w * 5, self.h * 5)
        if self.the_winner == 'Npc':
            self.font.draw(self.x - 200, self.y, f'You Lose', (0, 0, 0))
        elif self.the_winner == 'Player':
            self.font.draw(self.x - 180, self.y, f'You Win', (0, 0, 0))
        self.font2.draw(self.x - 150, self.y - 100, f'Press space to retry', (0, 0, 0))

    def update(self):
        pass
