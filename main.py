from pico2d import open_canvas, delay, close_canvas

import game_framework
import play_mode
import title_mode

open_canvas(800,550)
game_framework.run(play_mode)
delay(0.1)
close_canvas()
