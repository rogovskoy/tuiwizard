import time
import random
import os
from ..core.renderer import Renderer

def matrix_effect(duration=2.0):
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    end_time = time.time() + duration
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZアカサタナハマヤラワ"
    
    Renderer.hide_cursor()
    while time.time() < end_time:
        x = random.randint(1, width)
        y = random.randint(1, height)
        char = random.choice(chars)
        Renderer.move_cursor(x, y)
        print(Renderer.color(char, fg=46), end="", flush=True)
        time.sleep(0.01)
    Renderer.show_cursor()