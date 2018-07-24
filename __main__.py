import game
import curses
from curses import wrapper

def run(stdscr):
    # Some curses set up
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    #stdscr.bkgd(curses.COLOR_GREEN) <== figure out how to change the colors

    snakeGame = game.Game(stdscr)
    snakeGame.gameloop()
    

# Wrapper will take care of initializing and tearing down the curses session
wrapper(run)
