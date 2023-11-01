from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_UP, SDLK_DOWN


def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


class Idle:
    @staticmethod
    def enter(player, e):
        player.dir = 0
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
        player.y += player.dir * 15
        if player.y < 170 or player.y > 230:
            player.y -= player.dir * 15

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, player.frame * player.height + 72, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transitions = {
            Idle: {upkey_down: Swim, upkey_up: Swim, downkey_down: Swim, downkey_up: Swim},
            Swim: {upkey_down: Idle, upkey_up: Idle, downkey_down: Idle, downkey_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.player)


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
