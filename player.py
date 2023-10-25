from pico2d import load_image

import game_world


class Idle:
    @staticmethod
    def enter(player):
        player.frame = 0

    @staticmethod
    def exit(player):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 3

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.action, player.frame * player.height, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class Swim:
    @staticmethod
    def enter(player):
        pass

    @staticmethod
    def exit(player):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4

    @staticmethod
    def draw(player):
        player.image.clip_draw(0, player.frame * player.height + 72, player.width, player.height, player.x, player.y,
                               player.width * 4, player.height * 4)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.curstate = Idle

    def start(self):
        self.curstate.enter(self.player)

    def update(self):
        self.curstate.do(self.player)

    def draw(self):
        self.curstate.draw(self.player)


class Player:
    def __init__(self):
        self.image = load_image('redplayeranimation.png')
        self.x, self.y = 400, 200
        self.width, self.height = 24, 24
        self.frame = 0
        self.action = 0
        self.statemachine = StateMachine(self)
        self.statemachine.start()

    def draw(self):
        self.statemachine.draw()

    def update(self):
        self.statemachine.update()
