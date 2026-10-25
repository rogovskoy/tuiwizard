import sys
from ..core.renderer import Renderer

def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█', empty='░', color_code=46):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + empty * (length - filled_length)
    
    sys.stdout.write('\r' + ' ' * (len(prefix) + 50)) # Очистка остатков
    sys.stdout.write(f'\r{prefix} |{Renderer.color(bar, fg=color_code)}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total: 
        sys.stdout.write('\n')