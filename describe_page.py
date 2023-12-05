from pico2d import load_image, load_font


class Describe_Page:
    def __init__(self):
        self.image = load_image('Sprite/Background/background.png')
        self.x,self.y = 500,300
        self.w, self.h = self.image.w, self.image.h
        self.font = load_font('neodgm.ttf', 30)
        self.font2 = load_font('neodgm.ttf', 15)

    def draw(self):
        self.image.draw(self.x, self.y, self.w * 5, self.h * 5)
        self.font.draw(self.x - 450, self.y+200, f'~게임 설명~',(0,0,0))
        self.font.draw(self.x - 450, self.y+100, f'좌우 키를 눌러 빠르게 수영하세요',(0,0,0))
        self.font.draw(self.x - 450, self.y, f'위아래키를 눌러 아이템을 먹고 장애물을 피하세요',(0,0,0))
        self.font.draw(self.x - 450, self.y-100, f'5개이상의 아이템을 먹으면 스페이스바를 눌러 부스터를 쓰세요',(0,0,0))
        self.font2.draw(self.x + 200, self.y-250, f'스페이스를 눌러 게임을 시작 ->',(0,0,0))


    def update(self):
        pass