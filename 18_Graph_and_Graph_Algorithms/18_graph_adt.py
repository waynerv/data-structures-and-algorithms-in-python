class Vertex:
    def __init__(self, key):
        """在类的构造方法中，直接初始化id（key字符串）以及邻接字典。"""
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """添加邻接顶点，将邻接顶点对象以及相连边的权重作为参数传入"""
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """返回顶点的所有邻接顶点（的key），注意此返回结果为生成器"""
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWight(self, nbr):
        """通过邻接顶点对象在邻接字典中获取权重值"""
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        """在构造方法中初始化字典以及表示顶点个数的属性。"""
        self.vertList = {}
        self.numVertics = 0

    def addVertex(self, key):
        """构造并添加顶点到图中"""
        self.numVertics += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        """通过顶点key获取顶点对象，不存在返回None"""
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, start, end, wight=0):
        """添加从start顶点到end顶点的边并设置权重，若顶点在图中不存在则创建顶点并加入图中"""
        if start not in self.vertList:
            nv = self.addVertex(start)
        if end not in self.vertList:
            nv = self.addVertex(end)
        self.vertList[start].addNeighbor(self.vertList[end], wight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def test_graph():
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    assert len(g.vertList) == 6
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
