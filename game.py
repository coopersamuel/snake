import curses
import time

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.gameover = False

    def draw_tile(self, x, y, tile=''):
        self.screen.addstr(y, x, tile)

    def draw_map(self):
        self.screen.border(0)

    def get_input(self):
        # Make stdscr.getch non-blocking
        self.screen.nodelay(True)

        input = self.screen.getch()
        # Flush out anything else the user has typed in
        curses.flushinp()
        self.screen.clear()
            
        # Return a direction for the snake to start moving in
        if input == curses.KEY_DOWN:
            return 'down'
            #return (0, 1)
        elif input == curses.KEY_UP:
            return 'up'
            #return (0, -1)
        # elif input == curses.KEY_LEFT:
        #     #return (1, 0)
        # elif input == curses.KEY_RIGHT:
        #     #return (-1, 0)
        # elif input == ord('q'):
        #     #return 'q'

    def gameloop(self):
        counter = 0
        maxyx = self.screen.getmaxyx()
        center = (int(maxyx[1] / 2), int(maxyx[0] / 2))
        direction = 'up'

        while not self.gameover:
            self.draw_map()
            input = self.get_input() 
            direction = input if input else direction

            if direction == 'up':
                counter += 1
                self.draw_tile(center[0], center[1], str(counter))
            elif direction == 'down':
                counter -= 1
                self.draw_tile(center[0], center[1], str(counter))

            time.sleep(.3)