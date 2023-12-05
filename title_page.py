from pico2d import load_image, load_music


class Title_Page:
    def __init__(self):
        self.image = load_image('Sprite/Background/main_page.png')
        self.x, self.y = 500, 300
        self.bgm = load_music('Sound/bgm_menu.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
