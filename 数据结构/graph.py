# 节点
class Node:
    def __init__(self, name):
        """ name 为字符串 """
        self.name = name
    
    def __str__(self):
        return self.name


# 边
class Edge:
    def __init__(self, src, dest):
        """ src 为边的源头点，dest 为边的目标点 """
        self.src = src
        self.dest = dest

    def __str__(self):
        return '%s->%s' % (self.src, self.dest)


# 加权边
class WeightEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """ weight 为权重（长度） """
        Edge.__init__(self, src, dest)
        self.weight = weight

    def __str__(self):
        return '%s->(%.1f)%s' % (self.src, self.weight, self.dest)


# 有向图
class Digraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        """ node 为节点 """
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    
    def add_edge(self, edge):
        """ edge 为边 """
        src = edge.src
        dest = edge.dest
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def child_of(self, node):
        """ node 为父节点 """
        return self.edges[node]

    def has_node(self, node):
        """" node 为子节点 """
        return node in self.nodes

    def __str__(self):
        res = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                res += src + '->' + dest + '\n'
        return res[:-1]


# 无向图
class Graph(Digraph):
    def add_edge(self, edge):
        """ edge 为边 """
        Digraph.add_edge(self, edge)
        rev = Edge(edge.dest, edge.src)
        Digraph.add_edge(self, rev)