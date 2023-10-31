from pico2d import open_canvas, delay, close_canvas

import game_framework
import title_mode

open_canvas()
game_framework.run(title_mode)
delay(0.1)
close_canvas()
