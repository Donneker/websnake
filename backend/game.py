import random

from .snake import Snake

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.status = 'running'
        self.food = []
        self.score = 0

    def update(self):
        if self.status != 'running':
            return

        self.snake.move()

        # check if snake ate food
        if self.snake.body[0] in self.food:
            self.snake.ate_apple(1)
            self.score += 1
            self.food.remove(self.snake.body[0])
        else:
            self.snake.ate_apple(0)  # when no apple is eaten, the body is shortened

        # generate food if there is none
        if len(self.food) == 0:
            self.generate_food()

        if self.is_game_over():
            self.status = 'game-over'

    def generate_food(self):
        i = 0
        while ++i < 10:
            food_pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food_pos not in self.snake.body:
                self.food.append(food_pos)
                break

    def is_game_over(self):
        return self.snake.is_out_of_bounds(self.width, self.height) or self.snake.is_colliding_with_self()

    # Serialization method
    def to_json(self):
        return {
            'width': self.width,
            'height': self.height,
            'snake': self.snake.to_json(),
            'status': self.status,
            'food': self.food,
            'score': self.score
        }

    # Deserialization method
    @classmethod
    def from_json(cls, data):
        game = cls(data['width'], data['height'])
        game.snake = game.snake.from_json(data['snake'])
        game.status = data['status']
        game.food = data['food']
        game.score = data['score']
        return game

