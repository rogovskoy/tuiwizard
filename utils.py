import os

def get_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except OSError:
        return 80, 24

def safe_terminal_size(min_width=40, min_height=10):
    """Возвращает безопасный размер терминала, чтобы окна не вылезали за края."""
    w, h = get_terminal_size()
    return max(w, min_width), max(h, min_height)