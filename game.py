import curses
import time
import snake
import utils
from random import randint

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.gameover = False

    def get_input(self):
        # Make stdscr.getch non-blocking
        self.screen.nodelay(True)

        input = self.screen.getch()
        # Flush out anything else the user has typed in
        curses.flushinp()
        self.screen.clear()
            
        # Return a direction for the snake to start moving in
        if input == curses.KEY_DOWN:
            return (0, 1)
        elif input == curses.KEY_UP:
            return (0, -1)
        elif input == curses.KEY_LEFT:
            return (-1, 0)
        elif input == curses.KEY_RIGHT:
            return (1, 0)

    def spawn_apple(self):
        maxY, maxX = self.screen.getmaxyx()
        x = randint(1, maxX - 1)
        y = randint(1, maxY - 1)
        self.appleLocation = (x, y)

        '''
            TODO - Fix a bug where food won't spawn because it trys to spawn over top of the snake
        '''

    def draw_apple(self):
        utils.draw_tile(self.screen, self.appleLocation[0], self.appleLocation[1], '&')

    def eat_apple(self, snake):
        if snake.get_snake_location() == self.appleLocation:
            # Apple is eaten
            self.spawn_apple()
            snake.grow_snake()
        else:
            return

    def gameloop(self):
        gameSnake = snake.Snake(self.screen)
        self.spawn_apple()

        while not self.gameover:
            self.screen.border(0) # Draw the map
            direction = self.get_input() # Get user input
            
            if direction:
                # Only change direction if the user has given input
                gameSnake.change_direction(direction)

            gameSnake.move_snake()
            self.eat_apple(gameSnake)
            self.draw_apple()
            gameSnake.render_snake()

            time.sleep(.1) # This slows down the game speed