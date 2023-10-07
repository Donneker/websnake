# this is the snake class
# it should be json serializable so that it can be sent to the frontend
class Snake:
    def __init__(self):
        self.direction = 'right'
        self.body = [(5, 5)]
        self.ate_apples = 0

    def move(self):
        head = self.body[0]

        # movement against body direction is not allowed
        if len(self.body) > 2:
            bodydirection = 'undefined'
            bodyX = head[0] - self.body[1][0]
            bodyY = head[1] - self.body[1][1]
            if (bodyX >= 1):
                bodydirection = 'right'
            elif (bodyX <= -1):
                bodydirection = 'left'
            elif (bodyY >= 1):
                bodydirection = 'down'
            elif (bodyY <= -1):
                bodydirection = 'up'

            # correct direction if snake is trying to move backwards
            if (bodydirection == 'right' and self.direction == 'left'):
                self.direction = 'right'
            elif (bodydirection == 'left' and self.direction == 'right'):
                self.direction = 'left'
            elif (bodydirection == 'up' and self.direction == 'down'):
                self.direction = 'up'
            elif (bodydirection == 'down' and self.direction == 'up'):
                self.direction = 'down'

        if self.direction == 'right':
            self.body.insert(0, (head[0] + 1, head[1]))
        elif self.direction == 'left':
            self.body.insert(0, (head[0] - 1, head[1]))
        elif self.direction == 'up':
            self.body.insert(0, (head[0], head[1] - 1))
        elif self.direction == 'down':
            self.body.insert(0, (head[0], head[1] + 1))

    def ate_apple(self, apples):
        self.ate_apples += apples
        if self.ate_apples > 0:
            self.ate_apples -= 1
        else:
            self.body.pop()


    def is_out_of_bounds(self, width, height):
        head = self.body[0]
        return head[0] < 0 or head[1] < 0 or head[0] >= width or head[1] >= height

    def is_colliding_with_self(self):
        return self.body[0] in self.body[1:]

    # Serialization method
    def to_json(self):
        return {
            'direction': self.direction,
            'body': self.body,
            'ate_apples': self.ate_apples
        }

    # Deserialization method
    @classmethod
    def from_json(cls, data):
        snake = cls()
        snake.direction = data['direction']
        snake.body = data['body']
        snake.ate_apples = data['ate_apples']
        return snake
