from .game import Game

class Controller:
    def __init__(self):
        self.game = Game(20, 20)
        self.is_paused = False

    def update(self):
        if not self.is_paused:
            self.game.update()

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def newgame(self):
        self.game = Game(20, 20)
        self.is_paused = False

    def change_direction(self, direction):
        self.game.snake.direction = direction
