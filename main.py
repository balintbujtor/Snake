"""
Sources used for the implementation of the snake:

https://dr0id.bitbucket.io/legacy/pygame_tutorial01.html
https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
https://www.pygame.org/docs/ref/rect.html
https://www.codespeedy.com/movement-of-object-when-arrow-keys-are-pressed-in-pygame/
https://opensource.com/article/17/12/game-python-moving-player
https://stackoverflow.com/questions/31812433/pygame-sceen-fill-not-filling-up-the-color-properly
https://www.pygame.org/docs/tut/MoveIt.html

https://www.edureka.co/blog/snake-game-with-pygame/
https://gist.github.com/rajatdiptabiswas/bd0aaa46e975a4da5d090b801aba0611#file-snake-game-py-L141
https://dev.to/grapejuice/getting-started-with-pygame-making-a-snake-game-2i1g
"""

import pygame
import sys
import random

random.seed(69)


def snake():

    # variable init
    window_x = 480
    window_y = 480
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    rect_size = 15
    pos_x = random.randrange(1, window_x // rect_size) * rect_size
    pos_y = random.randrange(1, window_y // rect_size) * rect_size
    snake_body = [[pos_x, pos_y]]
    length = 1
    food_x = random.randrange(1, window_x // rect_size)*rect_size
    food_y = random.randrange(1, window_y // rect_size)*rect_size
    new_dir = 'right'
    direction = new_dir

    # game engine init
    pygame.init()
    fps_clock = pygame.time.Clock()
    dis = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption("SNAKE")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # checking key inputs
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            new_dir = 'left'
        elif key_input[pygame.K_RIGHT]:
            new_dir = 'right'
        elif key_input[pygame.K_UP]:
            new_dir = 'up'
        elif key_input[pygame.K_DOWN]:
            new_dir = 'down'

        # making sure not to move in opposite directions
        if new_dir == 'left' and direction != 'right':
            direction = 'left'
        elif new_dir == 'right' and direction != 'left':
            direction = 'right'
        elif new_dir == 'up' and direction != 'down':
            direction = 'up'
        elif new_dir == 'down' and direction != 'up':
            direction = 'down'

        # Moving the snake
        if direction == 'up':
            pos_y -= rect_size
        elif direction == 'down':
            pos_y += rect_size
        elif direction == 'left':
            pos_x -= rect_size
        elif direction == 'right':
            pos_x += rect_size

        # inserting new part to the snake every time it moves
        snake_body.insert(0, [pos_x, pos_y])

        # we only keep the new part if we ate the food otherwise we pop the oldest body part, making the movement
        if food_y == pos_y and food_x == pos_x:
            length += 1
            food_x = random.randrange(1, window_x // rect_size - rect_size) * rect_size
            food_y = random.randrange(1, window_y // rect_size - rect_size) * rect_size
        else:
            snake_body.pop()

        # clearing the screen
        dis.fill(white)

        # drawing the snake
        for rect in snake_body:
            pygame.draw.rect(dis, black, pygame.Rect(rect[0], rect[1], rect_size, rect_size))

        # drawing the food
        pygame.draw.rect(dis, red, pygame.Rect(food_x, food_y, rect_size, rect_size))

        # game over scenarios, going out of bounds
        if pos_x <= 0 or pos_y <= 0 or pos_x >= window_x or pos_y >= window_y:
            pygame.quit()
            sys.exit()

        # eating himself
        for part in snake_body[1:]:
            if pos_y == part[1] and pos_x == part[0]:
                pygame.quit()
                sys.exit()

        # updating the the game screen
        pygame.display.update()
        fps_clock.tick(10)


if __name__ == "__main__":
    snake()

# Create window
# Create the Snake
# Moving the Snake
# Game Over when Snake hits the boundaries
# Adding the Food
# Increasing the Length of the Snake
# opposite direction handling
# self eating handling
