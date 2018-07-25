import game
import curses
from curses import wrapper

def run(stdscr):
    # Some curses set up
    curses.curs_set(0)
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, -1)  #Default
    curses.init_pair(2, curses.COLOR_CYAN, -1) #Head
    curses.init_pair(3, curses.COLOR_RED, -1)    #Apple
    curses.init_pair(4, curses.COLOR_GREEN, -1)  #Body
    #stdscr.bkgd(curses.COLOR_GREEN) <== figure out how to change the colors

    snakeGame = game.Game(stdscr)
    snakeGame.gameloop()
    

# Wrapper will take care of initializing and tearing down the curses session
wrapper(run)
