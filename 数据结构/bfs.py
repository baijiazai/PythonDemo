"""
      B---D---F
     /   /|
    A   / |
     \ /  |
      C---E
"""

graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}


# 广度优先搜索
def bfs(graph, start):
    """ graph 为无向图，start 为起始点 """
    queue = [start]  # 创建一个队列，并把起始点添加进去
    seen = {start}  # 创建一个集合为已经检查过的节点，并把起始点添加进去
    while len(queue):  # 只要队列不为空，就循环
        vertex = queue.pop(0)  # 把队列的头拿出来，作为检查点
        nodes = graph[vertex]  # 取出检查点的所有临节点
        for node in nodes:  # 遍历临节点
            if node not in seen:  # 判断该临节点是否检查过
                queue.append(node)  # 把该临节点加入队列
                seen.add(node)  # 该临节点为已检查过，并加入集合中
        print(vertex)  # 打印检查点


# 最短路径
def bfs_shortest(graph, start, end):
    """ graph 为无向图，start 为起始点，end 为结束点 """
    queue = [start]
    seen = {start}
    last_node = {start: None}  # 记录每个节点的上一个节点
    res = []
    while len(queue):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                last_node[node] = vertex  # 该临节点的上一个节点为 vertex
    while end != None:  # 当 end 不为 None 时循环
        res.insert(0, end)  # 在列表头部插入 end
        end = last_node[end]  # end 为 end 的上一个节点
    return res


graph2 = {
    'a': {'b': 5, 'c': 1},
    'b': {'a': 5, 'c': 2, 'd': 1},
    'c': {'a': 1, 'b': 2, 'd': 4, 'e': 8},
    'd': {'b': 1, 'c': 4, 'e': 3, 'f': 6},
    'e': {'c': 8, 'd': 3},
    'f': {'d': 6}
}


def dijkstra(graph, start, end):
    property_queue = [(0, start)]  # 优先队列
    seen = set()
    parent = {start: None}
    distance = {start: 0}  # 到达 start 到达 distance[i] 最短的距离
    while len(property_queue):
        property_queue.sort()  # 优先队列排序
        dist, vertex = property_queue.pop(0)  # 弹出优先队列第一项，dist 为起始点到弹出的点的距离，vertex 为检查的点
        seen.add(vertex)  # 弹出后才算当前节点已被检查过
        nodes = graph2[vertex].keys()
        for node in nodes:
            if node not in seen:
                # 因为一开始 distance 字典中没有 node 这个键，所以要加个判断
                # 起始点到检查点的距离 + 检查点到 node 的距离 < 起始点到 node 的距离
                if node not in distance or dist + graph2[vertex][node] < distance[node]:
                    property_queue.append((dist + graph2[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dist + graph2[vertex][node]
    res = []
    output = (res, distance[end])
    while end != None:
        res.insert(0, end)
        end = parent[end]
    return output


if __name__ == "__main__":
    # bfs(graph, 'a')
    # shortest = bfs_shortest(graph, 'f', 'e')
    # print('->'.join(shortest))
    shortest, distance = dijkstra(graph2, 'a', 'd')
    print('->'.join(shortest), distance)
