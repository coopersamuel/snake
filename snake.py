import utils

class Snake():
    def __init__(self, screen):
        maxyx = screen.getmaxyx()
        center = (int(maxyx[1] / 2), int(maxyx[0] / 2))

        self.screen = screen    # Will need to keep a reference to the screen here too
        self.snake = [(center[0], center[1])]   # The snake will be an array of positions (x,y) representing the location of each body segment
                                                # The first element in the array is the snake's head

        self.grow = True
        self.growCounter = 0
        self.direction = False  #The direction the snake is going, for example right is positive in the x direction and zero in the y (1, 0)
                                # We initialize the direction as false until the user chooses a direction

    def move_snake(self):
        if not self.direction:
            return

        if self.growCounter >= 10:
            self.grow = False
            self.growCounter = 0

        if not self.grow:
            # If the snake is not growing, remove the last item in the list
            self.snake = self.snake[:-1]
        else:
            # If the snake is growing, increment the growCounter
            self.growCounter += 1

        # Add the target cell to the front of the snake
        targetCell = tuple(map(lambda x, y: x + y, self.snake[0], self.direction))
        self.snake.insert(0, targetCell)

    def has_snake_collision(self):
        snakeLocation = self.get_snake_location()
        for index, segment in enumerate(self.snake):
            if index > 0 and snakeLocation == segment:
                return True

        return False

    def grow_snake(self):
        # When food is eaten, set grow to True
        self.grow = True

    def get_snake_location(self):
        return self.snake[0]

    def render_snake(self):
        for segment in self.snake:
            utils.draw_tile(self.screen, segment[0], segment[1], 'o')

    def change_direction(self, direction):
        if not direction:
            return

        targetCell = tuple(map(lambda x, y: x + y, self.snake[0], direction))

        if len(self.snake) > 1 and self.snake[1] == targetCell:
            # Don't let the snake move backward on it self
            return

        self.direction = direction
