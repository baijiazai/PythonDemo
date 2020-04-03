import pygame
import random

W = 800
H = 600
size = (W, H)
cell = 20
col = W / cell
row = H / cell


class Food:
    def __init__(self, snake):
        self.x = random.randint(0, col - 1)
        self.y = random.randint(0, row - 1)
        self.color = (255, 0, 0)
        while True:
            if (self.x, self.y) in snake.body:
                self.x = random.randint(0, col - 1)
                self.y = random.randint(0, row - 1)
            else:
                break

    def create(self):
        pygame.draw.rect(window, self.color, (self.x * cell, self.y * cell, cell, cell))


class Snake:
    def __init__(self):
        self.body = [(3, 1), (2, 1), (1, 1)]
        self.dir = 'right'
        self.color = (0, 0, 255)

    def eat(self, food):
        return self.body[0][0] == food.x and self.body[0][1] == food.y

    def move(self, is_eat):
        old_head = self.body[0]
        if not is_eat:
            self.body.pop()
        if self.dir == 'left':
            self.body.insert(0, (old_head[0] - 1, old_head[1]))
        elif self.dir == 'right':
            self.body.insert(0, (old_head[0] + 1, old_head[1]))
        elif self.dir == 'up':
            self.body.insert(0, (old_head[0], old_head[1] - 1))
        elif self.dir == 'down':
            self.body.insert(0, (old_head[0], old_head[1] + 1))

    def die(self):
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head[0] == self.body[i][0] and head[1] == self.body[i][1]:
                return True
        return head[0] < 0 or head[0] == col or head[1] < 0 or head[1] == row

    def create(self):
        for body in self.body:
            pygame.draw.rect(window, self.color, (body[0] * cell, body[1] * cell, cell, cell))


pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption('贪吃蛇')
clock = pygame.time.Clock()

snake = Snake()
food = Food(snake)
mark = 0
quit = True

while quit:
    pygame.draw.rect(window, (255, 255, 255), (0, 0, W, H))
    food.create()
    snake.create()
    is_eat = snake.eat(food)
    snake.move(is_eat)

    if is_eat:
        food = Food(snake)
        mark += 1

    if snake.die():
        quit = False
        print('game over\nmark :', mark)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 273 or event.key == 119:
                if snake.dir != 'down':
                    snake.dir = 'up'
            elif event.key == 274 or event.key == 115:
                if snake.dir != 'up':
                    snake.dir = 'down'
            elif event.key == 276 or event.key == 97:
                if snake.dir != 'right':
                    snake.dir = 'left'
            elif event.key == 275 or event.key == 100:
                if snake.dir != 'left':
                    snake.dir = 'right'

    pygame.display.flip()
    clock.tick(10)
