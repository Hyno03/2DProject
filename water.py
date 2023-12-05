from pico2d import load_image, get_time, clamp, draw_rectangle, load_music

import game_framework
import game_world

WATER_TIME_PER_ACTION = 0.1
WATER_ACTION_PER_TIME = 1.0 / WATER_TIME_PER_ACTION

class Water_Background:
    def __init__(self, y = 0):
        self.image = load_image('Sprite/Background/water.png')
        self.x, self.y = 500, y
        self.w, self.h = self.image.w, self.image.h
        self.left_screen = 600
        self.frames_per_action = 8
        self.time = get_time()
        self.bgm = load_music('Sound/bgm_action_1.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y, self.w*2, self.h*2)
        self.image.draw(self.x + 1200, self.y, self.w*2, self.h*2)

    def update(self):
        self.x -= WATER_ACTION_PER_TIME * self.frames_per_action * game_framework.frame_time
        if self.x < -self.left_screen:
            self.x = self.left_screen
        if get_time() - self.time > 1:
            self.frames_per_action = 8

class Line:
    def __init__(self, y = 0):
        self.image = load_image('Sprite/Background/line.png')
        self.x, self.y = 100, y
        self.w, self.h = self.image.w, self.image.h

    def draw(self):
        self.image.draw(self.x, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 220, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 450, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 650, self.y, self.w * 4, self.h * 4)
        self.image.draw(self.x + 800, self.y, self.w * 4, self.h * 4)

    def update(self):
        pass


class Finish_Line:
    def __init__(self):
        self.image = load_image('Sprite/Background/floor2.png')
        self.x, self.y = 1300, 250
        self.w, self.h = self.image.w, self.image.h
        self.frames_per_action = 4
        self.time = get_time()
        self.the_winner = None
        self.is_swim_finish = {'Npc1': False, 'Player': False}
        game_world.add_collision_pair('player:end', None, self)
        game_world.add_collision_pair('npc:end', None, self)
        game_world.add_collision_pair('end:box', self, None)
        game_world.add_collision_pair('end:item', self, None)


    def draw(self):
        if get_time() - self.time > 30:
            self.image.draw(self.x, self.y, self.w * 2, self.h * 2)
            self.image.draw(self.x, self.y + 300, self.w * 2, self.h * 2)
            self.image.draw(self.x+140, self.y, self.w * 2, self.h * 2)
            self.image.draw(self.x+140, self.y + 300, self.w * 2, self.h * 2)
            self.image.draw(self.x+280, self.y, self.w * 2, self.h * 2)
            self.image.draw(self.x+280, self.y + 300, self.w * 2, self.h * 2)
            self.image.draw(self.x+420, self.y, self.w * 2, self.h * 2)
            self.image.draw(self.x+420, self.y + 300, self.w * 2, self.h * 2)
            # draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= WATER_ACTION_PER_TIME * self.frames_per_action * game_framework.frame_time
        self.x = clamp(900, self.x, 1300)

    def get_bb(self):
        return self.x-70, self.y-450, self.x + 200, self.y + +450

    def handle_collision(self, group, other):
        if group == 'player:end':
            if self.the_winner is None:
                self.the_winner = 'Player'
            self.is_swim_finish['Player'] = True
        if group == 'npc:end':
            if self.the_winner is None:
                self.the_winner = 'Npc'
            self.is_swim_finish['Npc1'] = True
        if group == 'end:box':
            pass
        if group == 'end:item':
            pass