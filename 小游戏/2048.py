import sys
import os
import random


def move(lst, direct=0):
    return ([0, 0, 0, 0] + [n for n in lst if n]
            )[-4:] if direct else ([n for n in lst if n] + [0, 0, 0, 0])[:4]


def sum_lst(lst, direct=0):
    if lst[1] and lst[2] and lst[1] == lst[2]:
        return move([lst[0], lst[1] * 2, 0, lst[3]], direct=direct)
    if lst[0] and lst[1] and lst[0] == lst[1]:
        lst[0], lst[1] = lst[0] * 2, 0
    if lst[2] and lst[3] and lst[2] == lst[3]:
        lst[2], lst[3] = lst[2] * 2, 0
    return move(lst, direct=direct)


def up(grid):
    for col in range(4):
        for r, n in enumerate(sum_lst(move([row[col] for row in grid]))):
            grid[r][col] = n
    return grid


def down(grid):
    for col in range(4):
        for r, n in enumerate(sum_lst(move([row[col] for row in grid], direct=1), direct=1)):
            grid[r][col] = n
    return grid


def left(grid):
    return [sum_lst(move(row)) for row in grid]


def right(grid):
    return [sum_lst(move(row, direct=1), direct=1) for row in grid]


class Game:
    def __init__(self):
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.controls = ['w', 'a', 's', 'd']

    def random_number(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while self.grid[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.grid[row][col] = 2 if random.random() < 0.5 else 4

    def print_grid(self):
        os.system('cls')
        print('-' * 21)
        for r in self.grid:
            print('|{}|'.format('|'.join([str(c or ' ').center(4) for c in r])))
            print('-' * 21)

    def logic(self, control):
        grid = {'w': up, 'a': left, 's': down, 'd': right}[
            control]([[c for c in r] for r in self.grid])
        if grid != self.grid:
            del self.grid[:]
            self.grid.extend(grid)
            for r in self.grid:
                for c in r:
                    if c >= 2048:
                        self.print_grid()
                        return 1, 'You Win!'
            self.random_number()
        else:
            if not [1 for g in [f(grid) for f in [up, down, left, right]] if g != self.grid]:
                return -1, 'You Lost!'
        return 0, ''

    def main_loop(self):
        self.random_number()
        self.random_number()
        while True:
            self.print_grid()
            control = input('input w/a/s/d:')
            if control in self.controls:
                status, info = self.logic(control)
                if status:
                    print(info)
                    if input('Start anthor game?[y/n]').lower() == 'y':
                        break
                    else:
                        sys.exit(0)
        self.__init__()
        self.main_loop()


if __name__ == "__main__":
    Game().main_loop()
