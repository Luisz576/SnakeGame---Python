# IMPORTS
import pygame

from pygame.locals import *
from sys import exit
from apple import Apple
from snake import Snake

# INIT
pygame.init()

# CONSTS
GAME_NAME = "SNAKE GAME"
BIG_FONT = pygame.font.SysFont('arial', 35, True, False)
SMALL_FONT = pygame.font.SysFont('arial', 20, True, False)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

GRID_DIMENSIONS = int(SCREEN_WIDTH / 16)

# WINDOW
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)


def eat_apple():
    global _gameScore, apple, snake
    _gameScore += 1
    snake.grow()


def _had_snake_left():
    global snake
    return (snake.get_position()[0] < 0 or snake.get_position()[0] >= SCREEN_WIDTH or snake.get_position()[1] < 0
            or snake.get_position()[1] >= SCREEN_HEIGHT)


def end_game():
    global _gameRunning
    _gameRunning = False


def reset():
    global _gameRunning, _gameScore, snake, apple
    _gameScore = 0
    snake.reset_snake()
    apple.reset_apple()
    _gameRunning = True


# VARS
clock = pygame.time.Clock()

_gameRunning = True
_gameScore = 0

snake = Snake(GRID_DIMENSIONS, window, end_game, 5,
              [(GRID_DIMENSIONS * 10, GRID_DIMENSIONS * 10), (GRID_DIMENSIONS * 9, GRID_DIMENSIONS * 10)])
apple = Apple((SCREEN_WIDTH, SCREEN_HEIGHT, GRID_DIMENSIONS), window,
              (GRID_DIMENSIONS * 5, GRID_DIMENSIONS * 5), eat_apple)

# GAME LOOP
while True:
    # TIME
    clock.tick(20)
    # CLEAR
    window.fill((0, 0, 0))
    # EVENTS
    for event in pygame.event.get():
        # EXIT
        if event.type == QUIT:
            pygame.quit()
            exit()
        # CONTROLLER
        if event.type == KEYDOWN:
            if event.key == K_w:
                snake.set_direction(0)
            if event.key == K_d:
                snake.set_direction(1)
            if event.key == K_s:
                snake.set_direction(2)
            if event.key == K_a:
                snake.set_direction(3)
            if event.key == K_SPACE and not _gameRunning:
                reset()
    if _gameRunning:
        # OBJECTS
        snake.update()
        apple.update(snake)
        window.blit(SMALL_FONT.render(f"Score: {_gameScore}00", True, (255, 255, 255)), (25, 25))
        if _had_snake_left():
            end_game()
    else:
        window.blit(BIG_FONT.render("GAME OVER", True, (255, 255, 255)),
                    (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))
        window.blit(SMALL_FONT.render(f"Score: {_gameScore}00", True, (255, 255, 255)),
                    (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2))
    # UPDATE
    pygame.display.update()
