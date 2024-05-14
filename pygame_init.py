import pygame_init
import sys
import random

# Initialize Pygame
pygame_init.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def check_collision(self):
        head_x, head_y = self.body[0]
        return (
            head_x < 0
            or head_x >= GRID_WIDTH
            or head_y < 0
            or head_y >= GRID_HEIGHT
            or self.body.count((head_x, head_y)) > 1
        )

    def grow(self):
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

    def draw(self, screen):
        for segment in self.body:
            pygame_init.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))


# Food class
class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def respawn(self):
        self.position = self.random_position()

    def draw(self, screen):
        pygame_init.draw.rect(screen, RED, (*self.position, GRID_SIZE, GRID_SIZE))


# Main function
def main():
    screen = pygame_init.display.set_mode((WIDTH, HEIGHT))
    pygame_init.display.set_caption("Snake Game")
    clock = pygame_init.time.Clock()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame_init.event.get():
            if event.type == pygame_init.QUIT:
                pygame_init.quit()
                sys.exit()
            elif event.type == pygame_init.KEYDOWN:
                if event.key == pygame_init.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame_init.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame_init.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame_init.K_RIGHT:
                    snake.change_direction(1, 0)

        snake.move()
        if snake.check_collision():
            print("Game Over!")
            pygame_init.quit()
            sys.exit()

        if snake.body[0] == food.position:
            snake.grow()
            food.respawn()

        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)
        pygame_init.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
