from pico2d import load_image, get_time, draw_rectangle
import random
import game_framework
import game_world

# Item Action Speed
TIME_PER_ACTION = 0.1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Item:
    def __init__(self):
        self.image = load_image('Sprite/Item/item.png')
        self.x, self.y = 900, 155
        self.w, self.h = 16, 16
        self.frame = 0
        self.time = get_time()
        self.item_drop = False
        self.random_time = random.randint(5,8)
        game_world.add_collision_pair('player:item', None, self)
        game_world.add_collision_pair('end:item', None, self)

    def draw(self):
        if self.item_drop:
            self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y, self.w * 2.5, self.h * 2.5)
            draw_rectangle(*self.get_bb())

    def update(self):
        if not self.item_drop and get_time() - self.time > self.random_time:
            self.item_drop = True
            new_item = Item()
            game_world.add_object(new_item, 1)
            self.random_time = random.randint(1,5)
            self.y = random.choice([100, 155, 210])
            self.time = get_time()

        if self.item_drop:
            self.x -= ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time
        if self.x < 0:
            game_world.remove_object(self)
            self.x = 550
            self.item_drop = False

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'player:item':
            game_world.remove_object(self)
        if group == 'end:item':
            game_world.remove_object(self)


class Obstacle:
    def __init__(self):
        self.image = load_image('Sprite/Item/Box1.png')
        self.x, self.y = 900, 165
        self.w, self.h = 32, 32
        self.frame = 0
        self.time = get_time()
        self.obstacle_drop = False
        self.random_time = random.randint(3,6)
        game_world.add_collision_pair('player:box', None, self)
        game_world.add_collision_pair('end:box', None, self)

    def draw(self):
        if self.obstacle_drop:
            self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)
            draw_rectangle(*self.get_bb())

    def update(self):
        if not self.obstacle_drop and get_time() - self.time > self.random_time:
            self.obstacle_drop = True
            new_obstacle = Obstacle()
            game_world.add_object(new_obstacle, 1)
            self.random_time = random.randint(1,5)
            self.y = random.choice([110,165,220])
            self.time = get_time()

        if self.obstacle_drop:
            self.x -= ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time
        if self.x < 0:
            game_world.remove_object(self)
            self.x = 550
            self.obstacle_drop = False

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 0

    def handle_collision(self, group, other):
        if group == 'player:box':
            self.x += ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time
        if group == 'end:box':
            game_world.remove_object(self)
