"""
        长沙 --- 武汉
       /   \        \ 
    广州 --- 南昌 --- 南京
       \            /
        福州 --- 杭州
"""
"""
        区间               距离（公里）    限速（公里 / 小时）      价格（元 / 公里）
    广州（0）- 长沙（1）     700           120                     0.8
    广州（0）- 南昌（2）     800           100                     0.9
    广州（0）- 福州（3）     850           120                     0.8
    长沙（1）- 武汉（4）     300           120                     0.7
    长沙（1）- 南昌（2）     250           120                     0.6
    南昌（2）- 南京（5）     600           100                     0.8
    福州（3）- 杭州（6）     700           120                     0.6
    武汉（4）- 南京（5）     700           120                     0.65
    杭州（6）- 南京（5）     300           120                     0.6
"""


class Edge:
    def __init__(self, src, dest, length, speed, price):
        self.src = src
        self.dest = dest
        self.length = length
        self.speed = speed
        self.price = price


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, edge):
        if edge.src in self.nodes and edge.dest in self.nodes:
            self.edges[edge.src].append((edge.dest, edge.length, edge.speed, edge.price))
            self.edges[edge.dest].append((edge.src, edge.length, edge.speed, edge.price))


def g_map():
    g = Graph()
    citys = ['广州', '长沙', '南昌', '福州', '武汉', '南京', '杭州']
    for city in citys:
        g.add_node(city)
    edges = [
        Edge('广州', '长沙', 700, 120, 0.8),
        Edge('广州', '南昌', 800, 100, 0.9),
        Edge('广州', '福州', 850, 120, 0.8),
        Edge('长沙', '武汉', 300, 120, 0.7),
        Edge('长沙', '南昌', 250, 120, 0.6),
        Edge('南昌', '南京', 600, 100, 0.8),
        Edge('福州', '杭州', 700, 120, 0.6),
        Edge('武汉', '南京', 700, 120, 0.65),
        Edge('杭州', '南京', 300, 120, 0.6),
    ]
    for edge in edges:
        g.add_edge(edge)
    return g


def bfs(graph, start, end, key_func=None):
    property_queue = [(0, start)]
    seen = set()
    parent = {start: None}
    total = {start: 0}
    while len(property_queue):
        property_queue.sort()
        weight, check = property_queue.pop(0)
        seen.add(check)
        nodes = graph.edges[check]
        for node in nodes:
            if node[0] not in seen:
                node_weight = key_func(node) if key_func else 1
                if node[0] not in total or weight + node_weight < total[node[0]]:
                    property_queue.append((weight + node_weight, node[0]))
                    parent[node[0]] = check
                    total[node[0]] = weight + node_weight
    path = []
    res = (path, total[end])
    while end != None:
        path.insert(0, end)
        end = parent[end]
    return res


if __name__ == "__main__":
    graph = g_map()
    path, total = bfs(graph, '广州', '南京')
    print('经过城市最少的线路：%s；经过 %d 个城市' % ('->'.join(path), total))
    path, total = bfs(graph, '广州', '南京', key_func=lambda item: item[1] * item[3])
    print('花费最少的线路：%s；花费 %.2f 元' %( '->'.join(path), total))
    path, total = bfs(graph, '广州', '南京', key_func=lambda item: item[1] / item[2])
    print('用时最少的线路：%s；用了 %.2f 小时' % ('->'.join(path), total))
