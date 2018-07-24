import utils

class Snake():
    def __init__(self, screen):
        maxyx = screen.getmaxyx()
        center = (int(maxyx[1] / 2), int(maxyx[0] / 2))

        self.screen = screen    # Will need to keep a reference to the screen here too
        self.snake = [] # The snake will be an array of positions (x,y) representing the location of each body segment
                        # The first element in the array is the snake's head

        for number in range(0, 5):
            self.snake.append((center[0] - number, center[1]))

        self.direction = False  #The direction the snake is going, for example right is positive in the x direction and zero in the y (1, 0)
                                # We initialize the direction as false until the user chooses a direction

    def move_snake(self):
        if not self.direction:
            return

        # First remove the last item in the list
        self.snake = self.snake[:-1]

        # Add the target cell to the front of the snake
        targetCell = tuple(map(lambda x, y: x + y, self.snake[0], self.direction))
        self.snake.insert(0, targetCell)


    def render_snake(self):
        for segment in self.snake:
            utils.draw_tile(self.screen, segment[0], segment[1], 'o')

    def change_direction(self, direction):
        if not direction:
            return

        targetCell = tuple(map(lambda x, y: x + y, self.snake[0], direction))

        if self.snake[1] == targetCell:
            # Don't let the snake move backward on it self
            return

        self.direction = direction
