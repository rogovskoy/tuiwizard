from ..core.renderer import Renderer
from ..core.input import get_key
import sys

class Menu:
    def __init__(self, options, title="Menu"):
        self.options = options
        self.title = title
        self.selected_index = 0

    def render(self, x=2, y=2):
        Renderer.move_cursor(x, y)
        print(Renderer.color(f"--- {self.title} ---", fg=15, style='bold'))
        
        for i, option in enumerate(self.options):
            Renderer.move_cursor(x, y + i + 2)
            if i == self.selected_index:
                print(Renderer.color(f"> {option} ", fg=0, bg=15))
            else:
                print(Renderer.color(f"  {option} ", fg=15, bg=None))
        sys.stdout.flush()

    def run(self, x=2, y=2):
        Renderer.hide_cursor()
        while True:
            self.render(x, y)
            key = get_key()
            if key == 'UP' and self.selected_index > 0:
                self.selected_index -= 1
            elif key == 'DOWN' and self.selected_index < len(self.options) - 1:
                self.selected_index += 1
            elif key == '\r' or key == '\n':
                Renderer.show_cursor()
                return self.options[self.selected_index]