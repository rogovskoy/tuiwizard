import sys

class Renderer:
    @staticmethod
    def clear():
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

    @staticmethod
    def move_cursor(x, y):
        sys.stdout.write(f"\033[{y};{x}H")
        sys.stdout.flush()

    @staticmethod
    def hide_cursor():
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    @staticmethod
    def show_cursor():
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    @staticmethod
    def color(text, fg=None, bg=None, style=None):
        codes = []
        if style == 'bold': codes.append("1")
        if style == 'underline': codes.append("4")
        if fg is not None: codes.append(f"38;5;{fg}")
        if bg is not None: codes.append(f"48;5;{bg}")
        
        if not codes:
            return text
        return f"\033[{';'.join(codes)}m{text}\033[0m"