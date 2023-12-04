from pico2d import load_image, load_font, SDL_KEYDOWN, SDLK_LEFT, SDLK_RIGHT, get_events, clamp


class Character_Select:
    def __init__(self):
        self.black_player = load_image('Sprite/Player/blackplayeranimation.png')
        self.blue_player = load_image('Sprite/Player/blueplayeranimation.png')
        self.red_player = load_image('Sprite/Player/redplayeranimation.png')
        self.x, self.y = 500, 260
        self.w, self.h = 24, 24
        self.main_font = load_font('neodgm.ttf', 60)
        self.sub_font = load_font('neodgm.ttf', 25)
        self.frame = 0

    def draw(self):
        self.red_player.clip_draw(0, self.frame * self.h, self.w, self.h, self.x - 250, self.y, self.w * 4, self.h * 4)
        self.blue_player.clip_draw(0, self.frame * self.h, self.w, self.h, self.x, self.y, self.w * 4, self.h * 4)
        self.black_player.clip_draw(0, self.frame * self.h, self.w, self.h, self.x + 250, self.y, self.w * 4, self.h * 4)
        self.main_font.draw(self.x - 300, self.y + 200, f'Choose your character', (0, 0, 0))
        self.sub_font.draw(self.x + 150, self.y - 220, f'Enter space to play game >', (0, 0, 0))

    def update(self):
        pass

class Select_Box:
    def __init__(self):
        self.image = load_image('Sprite/Background/select_box.png')
        self.x, self.y = 500, 260
        self.w, self.h = self.image.w / 1.5, self.image.h
        self.image2 = load_image('Sprite/Background/background.png')

    def draw(self):
        self.image.draw(self.x, self.y, self.w * 4, self.h * 4)
        self.image2.draw(self.x, self.y, self.w * 3.5, self.h * 3.6)

    def update(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                self.x += 250
            elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                self.x -= 250
        self.x = clamp(250, self.x, 750)