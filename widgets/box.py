from ..core.renderer import Renderer

def draw_box(x, y, width, height, title="", fg=15, bg=8, border_color=15):
    Renderer.move_cursor(x, y)
    print(Renderer.color("┌" + "─" * (width - 2) + "┐", fg=border_color))
    
    for i in range(1, height - 1):
        Renderer.move_cursor(x, y + i)
        print(Renderer.color("│", fg=border_color), end="")
        Renderer.move_cursor(x + 1, y + i)
        print(Renderer.color(" " * (width - 2), fg=fg, bg=bg), end="")
        Renderer.move_cursor(x + width - 1, y + i)
        print(Renderer.color("│", fg=border_color))
        
    Renderer.move_cursor(x, y + height - 1)
    print(Renderer.color("└" + "─" * (width - 2) + "┘", fg=border_color))
    
    if title:
        Renderer.move_cursor(x + 2, y)
        print(Renderer.color(f" {title} ", fg=fg, bg=bg))