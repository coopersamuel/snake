class Snake():
    def __init__(self):
        self.startX, self.startY = map.get_center()

        self.snake = [(startX, startY)]  # The snake will be an array of positions (x,y) representing the location of each body segment
        self.direction = (0, 0) # The direction the snake is going, for example right is positive in the x direction and zero in the y (1, 0)
                                # We initialize the snake as not moving so that the player can choose the snake's initial direction

    def moveSnake(self):
