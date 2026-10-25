import sys
import time
from ..core.renderer import Renderer

def typewriter(text, delay=0.03, color_code=None):
    if color_code:
        text = Renderer.color(text, fg=color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def text_shadow(text, fg=15, bg_shadow=240):
    shadow = Renderer.color(" " * len(text), bg=bg_shadow)
    print(shadow)
    print(Renderer.color(text, fg=fg))