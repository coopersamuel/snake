import curses
import time
import snake
import utils
from random import randint

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.playing = True
        self.score = 0
        self.highScore = 0

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
        elif input == ord(' '):
            self.reset()
        elif input == ord('q'):
            self.playing = False

    def spawn_apple(self):
        maxY, maxX = self.screen.getmaxyx()
        x = randint(1, maxX - 2)
        y = randint(1, maxY - 2)
        self.appleLocation = (x, y)

        for segment in self.gameSnake.snake:
            if self.appleLocation == segment:
                # Don't spawn food on top of the snake
                # If this happens, try again
                self.spawn_apple()

    def draw_apple(self):
        utils.draw_tile(self.screen, self.appleLocation[0], self.appleLocation[1], '&')

    def eat_apple(self):
        if self.gameSnake.get_snake_location() == self.appleLocation:
            # Apple is eaten
            self.spawn_apple()
            self.gameSnake.grow_snake()
            self.score += 1
            if self.score > self.highScore:
                self.highScore += 1
        else:
            return

    def has_border_collision(self):
        snakeLocation = self.gameSnake.get_snake_location()
        maxY, maxX = self.screen.getmaxyx()

        if snakeLocation[0] == 0 or snakeLocation[0] == maxX - 1 or snakeLocation[1] == 0 or snakeLocation[1] == maxY - 1:
            return True

        return False

    def draw_gameover(self):
        maxyx = self.screen.getmaxyx()
        center = (int(maxyx[1] / 2), int(maxyx[0] / 2))

        utils.draw_tile(self.screen, center[0] - 22, center[1] - 5, ' __              ___     __        ___  __  ')
        utils.draw_tile(self.screen, center[0] - 22, center[1] - 4, '/ _`  /\   |\/| |__     /  \ \  / |__  |__) ')
        utils.draw_tile(self.screen, center[0] - 22, center[1] - 3, '\__> /~~\  |  | |___    \__/  \/  |___ |  \ ')
        utils.draw_tile(self.screen, center[0] - 14, center[1] + 2, 'Space to restart, Q to quit')

    def draw_map(self):
        #self.screen.border(0) # Draw the map
        utils.draw_tile(self.screen, 5, 0, ' Score: %s ' %self.score)
        utils.draw_tile(self.screen, 20, 0, ' High Score: %s ' %self.highScore)

    def reset(self):
        self.score = 0
        self.spawn_apple()
        self.gameSnake = snake.Snake(self.screen)

    def gameloop(self):
        self.gameSnake = snake.Snake(self.screen)
        self.spawn_apple()

        while self.playing:
            self.draw_map()
            direction = self.get_input() # Get user input
            
            if direction:
                # Only change direction if the user has given input
                self.gameSnake.change_direction(direction)

            if not self.has_border_collision() and not self.gameSnake.has_snake_collision():
                self.gameSnake.move_snake()
                self.eat_apple()
                self.draw_apple()
                self.gameSnake.render_snake()
            else:
                self.draw_gameover()

            time.sleep(.1) # This slows down the game speed
