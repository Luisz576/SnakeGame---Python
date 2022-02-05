import pygame.draw

from random import randint


class Apple:
    def __init__(self, main_info, window, position, eat_apple):
        self.SCREEN_WIDTH = main_info[0]
        self.SCREEN_HEIGHT = main_info[1]
        self.GRID_DIMENSIONS = main_info[2]
        self.window = window
        self.color = (255, 0, 0)
        self.apple_draw = None
        self.position = position
        self.eat_apple = eat_apple
        self._start_position = (self.position[0], self.position[1])

    def _eat(self):
        self.position = ((randint(1, self.SCREEN_WIDTH / self.GRID_DIMENSIONS) - 1) * self.GRID_DIMENSIONS,
                         (randint(1, self.SCREEN_HEIGHT / self.GRID_DIMENSIONS) - 1) * self.GRID_DIMENSIONS)

    def reset_apple(self):
        self.position = self._start_position

    def update(self, snake):
        if self.apple_draw is not None and snake.snake_draw.colliderect(self.apple_draw):
            self._eat()
            self.eat_apple()
        self.apple_draw = pygame.draw.rect(self.window, self.color,
                                     (self.position[0], self.position[1], self.GRID_DIMENSIONS, self.GRID_DIMENSIONS))
