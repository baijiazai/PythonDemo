"""
      B---D---F    
     /   /|
    A   / |
     \ /  |
      C---E
"""

graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}


# 深度优先搜索
def dfs(graph, start):
    """ graph 为无向图，start 为起始点 """
    stack = [start]  # 创建一个栈，并把起始点加入栈中
    seen = {start}  # 创建一个集合为已经检查过的节点，并把起始点添加进去
    while len(stack):  # 只要栈不为空，就循环
        vertex = stack.pop()  # 把栈的顶部拿出来，作为检查点
        nodes = graph[vertex]  # 取出检查点的所有临节点
        for node in nodes:  # 遍历临节点
            if node not in seen:  # 判断该临节点是否已检查过
                stack.append(node)  # 把该临节点放入栈中
                seen.add(node)  # 该临节点为已检查过，并加入集合中
        print(vertex)  # 打印临节点


def dfs2(graph, start, path):
    if start in path: return
    path.append(start)
    for node in graph[start]:
        if node not in path:
            dfs2(graph, node, path)



# 最短路径
def dfs_shortest(graph, start, end):
    """ graph 为无向图，start 为起始点，end 为结束点 """
    stack = [start]
    seen = {start}
    last_node = {start: None}
    res = []
    while len(stack):
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
                last_node[node] = vertex
    while end != None:
        res.insert(0, end)
        end = last_node[end]
    return res


if __name__ == "__main__":
    # dfs(graph, 'a')
    shortest = dfs_shortest(graph, 'a', 'e')
    print('->'.join(shortest))
