import curses
import time
import snake
import utils

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

    def gameloop(self):
        gameSnake = snake.Snake(self.screen)

        while not self.gameover:
            self.screen.border(0) # Draw the map
            direction = self.get_input() # Get user input
            
            if direction:
                # Only change direction if the user has given input
                gameSnake.change_direction(direction)

            gameSnake.move_snake()
            gameSnake.render_snake()
            # if direction == 'up':
            #     counter += 1
            #     utils.draw_tile(self.screen, center[0], center[1], str(counter))
            # elif direction == 'down':
            #     counter -= 1
            #     utils.draw_tile(self.screen, center[0], center[1], str(counter))

            time.sleep(.1) # This slows down the game speed