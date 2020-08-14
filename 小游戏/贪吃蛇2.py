import os
import random
import time
from random import randint

ROW = 15
COL = 55

FOOD = 1
SNAKE_HEAD = 2
SNAKE_BODY = 3
WALL = 4


class Food:
    def __init__(self, world):
        blank_list = []
        for r in range(len(world)):
            for c in range(len(world[r])):
                if world[r][c] == 0:
                    blank_list.append((r, c))
        self.row, self.col = random.choice(blank_list)
        # self.row = randint(1, ROW - 1)
        # self.col = randint(1, COL - 1)
        # while world[self.row][self.col] != 0:
        #     self.row = randint(1, ROW - 1)
        #     self.col = randint(1, COL - 1)
        self.point = (self.row, self.col)

    def create(self, world):
        world[self.row][self.col] = FOOD


class Snake:
    def __init__(self):
        self.body = [(1, 3), (1, 2), (1, 1)]
        self.dir = 'r'

    def create(self, world):
        for i, b in enumerate(self.body):
            world[b[0]][b[1]] = SNAKE_HEAD if i == 0 else SNAKE_BODY

    def eat(self, food):
        return self.body[0] == food.point

    def move(self, is_eat, step):
        old_head = self.body[0]
        if not is_eat:
            self.body.pop()
        # self.body.insert(0, step)

        if old_head[0] < step[0] and self.dir != 'u':
            if (old_head[0] + 1, old_head[1]) in self.body:
                self.dir = random.choice(['l', 'r'])
            else:
                self.dir = 'd'
        elif old_head[0] > step[0] and self.dir != 'd':
            if (old_head[0] - 1, old_head[1]) in self.body:
                self.dir = random.choice(['l', 'r'])
            else:
                self.dir = 'u'
        elif old_head[1] < step[1] and self.dir != 'l':
            if (old_head[0], old_head[1] + 1) in self.body:
                self.dir = random.choice(['u', 'd'])
            else:
                self.dir = 'r'
        elif old_head[1] > step[1] and self.dir != 'r':
            if (old_head[0], old_head[1] - 1) in self.body:
                self.dir = random.choice(['u', 'd'])
            else:
                self.dir = 'l'

        if self.dir == 'l':
            self.body.insert(0, (old_head[0], old_head[1] - 1))
        elif self.dir == 'r':
            self.body.insert(0, (old_head[0], old_head[1] + 1))
        elif self.dir == 'u':
            self.body.insert(0, (old_head[0] - 1, old_head[1]))
        else:
            self.body.insert(0, (old_head[0] + 1, old_head[1]))

    def die(self, world):
        snake_head = self.body[0]
        against_the_wall = world[snake_head[0]][snake_head[1]] == WALL
        bite_to_self = world[snake_head[0]][snake_head[1]] == SNAKE_BODY
        return against_the_wall or bite_to_self

    def graph(self, world, point):
        snake_head = self.body[0]
        graph = {
            snake_head: [],
            point: []
        }

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        for r in range(ROW):
            for c in range(COL):
                if 0 < r < ROW - 1 and 0 < c < COL - 1 and world[r][c] == 0:
                    graph[(r, c)] = []
                    for i in range(4):
                        if world[r + dy[i]][c + dx[i]] == 0:
                            graph[(r, c)].append((r + dy[i], c + dx[i]))
        for i in range(4):
            if world[snake_head[0] + dy[i]][snake_head[1] + dx[i]] == 0:
                graph[snake_head].append((snake_head[0] + dy[i], snake_head[1] + dx[i]))
            if world[point[0] + dy[i]][point[1] + dx[i]] == 0:
                graph[point].append((point[0] + dy[i], point[1] + dx[i]))
        return graph

    def bfs(self, world, point):
        graph = self.graph(world, point)
        start = self.body[0]
        end = point
        queue = [start]
        seen = {start}
        parent = {start: None}
        while queue:
            vertex = queue.pop(0)
            nodes = graph[vertex]
            for node in nodes:
                if node not in seen:
                    queue.append(node)
                    seen.add(node)
                    parent[node] = vertex
        path = []
        try:
            while end is not None:
                path.insert(0, end)
                end = parent[end]
        except KeyError:
            path = []
        return path


class Game:
    mark = 0

    def __init__(self):
        self.world = [[WALL if r == 0 or r == ROW - 1 or c == 0 or c == COL - 1 else 0 for c in range(COL)]
                      for r in range(ROW)]

    def show(self):
        style = (' ', '$', '@', '*', '#')
        print('\n'.join([' '.join([style[c] for c in r]) for r in self.world]))

    def play(self):
        snake = Snake()
        food = Food(self.world)
        is_eat = False

        path = snake.bfs(self.world, food.point)
        path.pop(0)

        while True:
            self.__init__()

            snake.create(self.world)
            food.create(self.world)
            if path:
                snake.move(is_eat, path.pop(0))
            else:
                snake.move(is_eat, food.point)
                path = snake.bfs(self.world, food.point)
                if not path:
                    path = snake.bfs(self.world, snake.body[-1])
                if path:
                    path.pop(0)

            is_eat = snake.eat(food)
            if is_eat:
                food = Food(self.world)
                self.mark += 1
                path = snake.bfs(self.world, food.point)
                if not path:
                    path = snake.bfs(self.world, snake.body[-1])
                if path:
                    path.pop(0)

            os.system('cls')
            self.show()
            if snake.die(self.world):
                print('GAME OVER')
                print('mark:', self.mark)
                return
            time.sleep(0.1)


if __name__ == '__main__':
    Game().play()
