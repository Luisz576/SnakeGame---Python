import pygame


class Snake:
    def __init__(self, dimensions, window, end_game, ticks, positions):
        self.GRID_DIMENSIONS = dimensions
        self.window = window
        self.end_game = end_game
        # 0 - Up / 1 - Right / 2 - Down / 3 - Left
        self.direction = 0
        self.last_direction = self.direction
        self.color = (0, 255, 0)
        self.wait_ticks = ticks
        self.ticks = 0
        self.snake_draw = None
        self.body = []
        self.body_size = 0
        for position in positions:
            self.body.append(position)
            self.body_size += 1
        self._start_body = []
        self._start_body.extend(self.body)

    def reset_snake(self):
        self.body.clear()
        self.body.extend(self._start_body)
        self.body_size = len(self.body) - 1
        self.direction = 0
        self.snake_draw = None

    def set_direction(self, direction):
        if (direction == 0 and self.last_direction == 2) \
                or (direction == 1 and self.last_direction == 3) \
                or (direction == 2 and self.last_direction == 0) \
                or (direction == 3 and self.last_direction == 1):
            return
        self.direction = direction

    def grow(self):
        self.body_size += 1

    def _had_eat_self(self):
        i = 1
        for body_part in self.body:
            if i < len(self.body):
                if body_part[0] == self.get_position()[0] \
                        and body_part[1] == self.get_position()[1]:
                    return True
            i += 1
        return False

    def get_position(self):
        return self.body[len(self.body) - 1]

    def _draw(self):
        for part_body in self.body:
            self.snake_draw = pygame.draw.rect(self.window, self.color,
                                               (part_body[0], part_body[1], self.GRID_DIMENSIONS,
                                                self.GRID_DIMENSIONS))

    def update(self):
        if self._had_eat_self():
            self.end_game()
        self.ticks += 1
        if self.ticks >= self.wait_ticks:
            self.ticks = 0
            x = 0
            y = 0
            if self.direction == 0:
                y = -1
            elif self.direction == 1:
                x = 1
            elif self.direction == 2:
                y = 1
            elif self.direction == 3:
                x = -1
            self.body.append((self.body[len(self.body) - 1][0] + x * self.GRID_DIMENSIONS,
                              self.body[len(self.body) - 1][1] + y * self.GRID_DIMENSIONS))
            self.last_direction = self.direction
            if len(self.body) > self.body_size:
                del self.body[0]
        self._draw()
