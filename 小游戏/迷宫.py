import os
import random


class Maze:
    def __init__(self, width, height):
        """
        :初始化迷宫:
        :param width: 迷宫宽度，必须为奇数（int）
        :param height: 迷宫高度，必须为奇数（int）
        """
        self.width = width
        self.height = height
        self.map = [[0 if x % 2 == 1 and y % 2 == 1 else 1 for x in range(width)] for y in range(height)]
        self.map[1][0] = 0  # 入口
        self.map[height - 2][width - 1] = 0  # 出口
        self.visited = []
        # 方向：右、上、下、左
        self.dx = [1, 0, -1, 0]
        self.dy = [0, -1, 0, 1]

    def set_value(self, point, value):
        """
        :设置节点的值:
        :param point: 节点坐标（tuple）
        :param value: 值（int）
        """
        self.map[point[1]][point[0]] = value

    def get_value(self, point):
        """
        :获取节点的值:
        :param point: 节点坐标（tuple）
        :return: 节点的值（int）
        """
        return self.map[point[1]][point[0]]

    def show(self):
        """ 打印迷宫 """
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) == (1, 0) or (r, c) == (self.height - 2, self.width - 1):
                    s = ' '
                elif self.map[r][c] == 0:
                    s = '  '
                elif c == 0 or c == self.width - 1:
                    s = '|'
                elif 0 < r < self.height - 1 and 0 < c < self.width - 1 and \
                        self.map[r + 1][c] == 1 and self.map[r - 1][c] == 1:
                    s = '||'
                else:
                    s = '--'
                if self.map[r][c] == 2 and 0 < c < self.width - 1:
                    s = '**'
                print(s, end='')
            print()

    def get_neighbor(self, x, y, value):
        """
        :获取邻节点坐标列表:
        :param x: 列索引（int）
        :param y: 行索引（int）
        :param value: 目标值（int）
        :return: 邻节点坐标列表（list）
        """
        return [(x + self.dx[i], y + self.dy[i]) for i in range(4) if
                0 < x + self.dx[i] < self.width - 1 and 0 < y + self.dy[i] < self.height - 1 and self.get_value(
                    (x + self.dx[i], y + self.dy[i])) == value]

    def get_neighbor_wall(self, point):
        """
        :获取邻墙坐标列表:
        :param point: 节点坐标（tuple）
        :return: 邻墙坐标列表（list）
        """
        return self.get_neighbor(point[0], point[1], 1)

    def get_neighbor_road(self, point):
        """
        :获取邻路坐标列表:
        :param point: 节点坐标（tuple）
        :return: 邻路坐标列表（list）
        """
        return self.get_neighbor(point[0], point[1], 0)

    def deal_with_not_visited(self, point, wall_position, wall_list):
        """
        :打通墙体:
        :param point: 节点坐标（tuple）
        :param wall_position: 墙坐标（tuple）
        :param wall_list: 墙列表（list）
        """
        if not (point[0], point[1]) in self.visited:
            self.set_value(wall_position, 0)
            self.visited.append(point)
            wall_list.extend(self.get_neighbor_wall(point))

    def generate(self):
        """ :生成迷宫: """
        start = (1, 1)
        self.visited.append(start)
        wall_list = self.get_neighbor_wall(start)
        while wall_list:
            wall_position = random.choice(wall_list)
            neighbor_road = self.get_neighbor_road(wall_position)
            wall_list.remove(wall_position)
            self.deal_with_not_visited(neighbor_road[0], wall_position, wall_list)
            self.deal_with_not_visited(neighbor_road[1], wall_position, wall_list)

    def graph(self):
        """
        :生成道路图:
        :return: 道路字典（dict）
        """
        graph = {
            (1, 0): [(1, 1)],
            (self.height - 2, self.width - 1): [(self.height - 2, self.width - 2)]
        }
        for r in range(self.height):
            for c in range(self.width):
                if 0 < r < self.height - 1 and 0 < c < self.width - 1:
                    graph[(r, c)] = []
                    for i in range(4):
                        if self.map[r + self.dy[i]][c + self.dx[i]] == 0:
                            graph[(r, c)].append((r + self.dy[i], c + self.dx[i]))
        return graph

    def bfs(self):
        """ 利用广度优先搜索算法寻找出口 """
        graph = self.graph()
        start = (1, 0)
        end = (self.height - 2, self.width - 1)
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
        while end is not None:
            self.map[end[0]][end[1]] = 2
            end = parent[end]


if __name__ == '__main__':
    maze = Maze(55, 15)
    maze.generate()
    maze.show()
    input('按回车查看答案')
    os.system('cls')
    maze.bfs()
    maze.show()
