import time
import sys
from ..core.renderer import Renderer

def fade_in(text, x, y, duration=0.5):
    """Имитация плавного появления за счет смены цвета с темного на светлый."""
    steps = 10
    for i in range(steps + 1):
        # Вычисляем цвет от 232 (очень темный) до 255 (белый)
        color = 232 + int((255 - 232) * (i / steps))
        Renderer.move_cursor(x, y)
        print(Renderer.color(text, fg=color), end="", flush=True)
        time.sleep(duration / steps)
    print()