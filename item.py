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
        self.x, self.y = 550, 175
        self.w, self.h = 16, 16
        self.frame = 0
        self.time = get_time()
        self.item_drop = False
        self.random_time = random.randint(1,10)
        game_world.add_collision_pair('player:item', None, self)

    def draw(self):
        if self.item_drop == True:
            self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y, self.w * 3, self.h * 3)
            draw_rectangle(*self.get_bb())

    def update(self):
        if not self.item_drop and get_time() - self.time > 1:
            self.item_drop = True
            new_item = Item()
            game_world.add_object(new_item, 7)
            self.random_time = random.randint(1,5)
            self.time = get_time()

        if self.item_drop:
            self.x -= ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time
        if self.x < 0:
            game_world.remove_object(self)
            self.x = 550
            self.item_drop = False

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:item':
            game_world.remove_object(self)


