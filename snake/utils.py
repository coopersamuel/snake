import curses

def draw_tile(screen, x, y, tile='', color=None):
        screen.addstr(y, x, tile, color)