import curses

def draw_tile(screen, x, y, tile=''):
        screen.addstr(y, x, tile)