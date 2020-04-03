import os
import sys
import random


class Game:
    def __init__(self):
        self.gird = [[0 for _ in range(3)] for _ in range(3)]
        self.position = {}
        i = 0
        for row in range(2, -1, -1):
            for col in range(3):
                i += 1
                self.position[i] = (row, col)

    def get_gird(self, pos):
        return self.gird[self.position[pos][0]][self.position[pos][1]]

    def set_gird(self, pos, val):
        self.gird[self.position[pos][0]][self.position[pos][1]] = val

    def show(self, win=0):
        os.system('cls')
        print('-' * 13)
        for row in self.gird:
            print('|{}|'.format('|'.join(str(col or ' ').center(3)
                                         for col in row)))
            print('-' * 13)
        if win == 1:
            print('You Win!')
        elif win == 2:
            print('You Lost!')
        elif win == 3:
            print('Tie Game!')

    def player(self):
        while True:
            try:
                player = int(input('input number 1 - 9:'))
            except ValueError:
                continue
            if player in self.position and self.get_gird(player) == 0:
                break
        self.set_gird(player, 'o')

    def ai_k(self, who):
        for i in range(1, 10):
            if self.get_gird(i) == 0:
                ai_gird = [[col for col in row] for row in self.gird]
                ai_gird[self.position[i][0]][self.position[i][1]] = who
                for row in ai_gird:
                    if row[0] == row[1] == row[2] == who:
                        self.set_gird(i, 'x')
                        return 1
                for col in range(3):
                    if ai_gird[0][col] == ai_gird[1][col] == ai_gird[2][col] == who:
                        self.set_gird(i, 'x')
                        return 1
                if ai_gird[0][0] == ai_gird[1][1] == ai_gird[2][2] == who or ai_gird[2][0] == ai_gird[1][1] == ai_gird[0][2] == who:
                    self.set_gird(i, 'x')
                    return 1
        return 0

    def ai(self):
        if self.ai_k('x') or self.ai_k('o'):
            return
        ai = random.randint(1, 9)
        while self.get_gird(ai) != 0:
            ai = random.randint(1, 9)
        self.set_gird(ai, 'x')

    def winner(self):
        for row in self.gird:
            if row[0] ==  row[1] ==  row[2] == 'o':
                return 1
            if row[0] ==  row[1] ==  row[2] == 'x':
                return 2
        for col in range(3):
            if self.gird[0][col] ==  self.gird[1][col] ==  self.gird[2][col] == 'o':
                return 1
            if self.gird[0][col] ==  self.gird[1][col] ==  self.gird[2][col] == 'x':
                return 2
        if self.gird[0][0] == self.gird[1][1] == self.gird[2][2] == 'o' or self.gird[2][0] == self.gird[1][1] == self.gird[0][2] == 'o':
            return 1
        if self.gird[0][0] == self.gird[1][1] == self.gird[2][2] == 'x' or self.gird[2][0] == self.gird[1][1] == self.gird[0][2] == 'x':
            return 2
        for row in self.gird:
            for col in row:
                if col == 0:
                    return 0
        return 3

    def play(self):
        while True:
            self.show()
            self.player()
            if self.winner() != 0:
                self.show(self.winner())
                break
            self.ai()
            if self.winner() != 0:
                self.show(self.winner())
                break
        if input('Start anthor game?[y/N]:').lower() == 'y':
            self.__init__()
            self.play()
        else:
            sys.exit(0)


if __name__ == "__main__":
    Game().play()
