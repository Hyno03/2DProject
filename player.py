from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_UP, SDLK_DOWN


def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].type == SDLK_UP


def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].type == SDLK_UP


def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].type == SDLK_DOWN


def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].type == SDLK_DOWN


class Idle:
    @staticmethod
    def enter(player, e):
        player.frame = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 3

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, player.frame * player.height, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class Swim:
    @staticmethod
    def enter(player, e):
        if upkey_down(e) or downkey_up(e):
            player.dir = 1
        elif upkey_up(e) or downkey_down(e):
            player.dir = -1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        player.y += player.dir * 5

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, player.frame * player.height + 72, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.curstate = Idle
        self.transitions = {
            Idle: {upkey_down: Swim, downkey_down: Swim},
            Swim: {upkey_up: Idle, downkey_up: Idle}
        }

    def start(self):
        self.curstate.enter(self.player, ('NONE', 0))

    def update(self):
        self.curstate.do(self.player)

    def handle_event(self, e):
        pass

    def draw(self):
        self.curstate.draw(self.player)


class Player:
    def __init__(self):
        self.image = load_image('redplayeranimation.png')
        self.x, self.y = 400, 200
        self.width, self.height = 24, 24
        self.frame = 0
        self.dir = 0
        self.statemachine = StateMachine(self)
        self.statemachine.start()

    def handle_event(self, event):
        self.statemachine.handle_event(('INPUT', event))

    def draw(self):
        self.statemachine.draw()

    def update(self):
        self.statemachine.update()
