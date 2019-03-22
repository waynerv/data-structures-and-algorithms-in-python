import heapq
import itertools


class PriorityQueue(object):
    REMOVED = '<removed-task>'  # 被删除任务的占位字符

    def __init__(self):
        self.pq = []  # 初始化heapq所使用的list
        self.entry_finder = {}  # 任务到优先级条目的映射,用来快速的在队列中找到任务对应优先级条目
        self.counter = itertools.count()  # 唯一计数器

    def add_task(self, task, priority=0):
        """添加一个新任务或者更新一个已存在任务的优先级"""
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        """将一个已存在的任务标记为REMOVED，若未找到Raise KeyError。"""
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

    def pop_task(self):
        """删除并返回最小优先级任务，如果队列已空Raise KeyError"""
        while self.pq:  # 循环直到弹出值不为REMOVED的task才返回
            priority, count, task = heapq.heappop(self.pq)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def is_empty(self):
        return len(self.entry_finder) == 0

    def __contains__(self, item):
        return item in self.entry_finder


class Vertex:
    def __init__(self, key, distance=float('inf')):
        """
        在类的构造方法中，直接初始化id（key字符串）以及邻接字典。
        """
        self.id = key
        self.connectedTo = {}
        self.distance = distance
        self.predecessor = None

    def addNeighbor(self, nbr, weight=0):
        """
        添加邻接顶点，将邻接顶点对象以及相连边的权重作为参数传入
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def __lt__(self, other):
        pass

    def getConnections(self):
        """
        返回顶点的所有邻接顶点（的key），注意此返回结果为生成器
        """
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        """
        通过邻接顶点对象在邻接字典中获取权重值
        """
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance

    def setDistance(self, value):
        self.distance = value

    def getPred(self):
        return self.predecessor

    def setPred(self, value):
        self.predecessor = value


class Graph:
    def __init__(self):
        """
        在构造方法中初始化字典以及表示顶点个数的属性。
        """
        self.vertList = {}
        self.numVertics = 0

    def addVertex(self, key):
        """
        构造并添加顶点到图中
        """
        self.numVertics += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        """
        通过顶点key获取顶点对象，不存在返回None
        """
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, start, end, wight=0):
        """
        添加从start顶点到end顶点的边并设置权重，若顶点在图中不存在则创建顶点并加入图中
        """
        if start not in self.vertList:
            nv = self.addVertex(start)
        if end not in self.vertList:
            nv = self.addVertex(end)
        self.vertList[start].addNeighbor(self.vertList[end], wight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def prim(graph, start):
    # 构造优先级队列
    pq = PriorityQueue()
    start.setDistance(0)
    pq_list = [(v, v.getDistance()) for v in graph]
    for v, priority in pq_list:
        pq.add_task(v, priority)
    # 从队列中取出当前距离最小的顶点，更新其邻居节点的距离
    while not pq.is_empty():
        currentVert = pq.pop_task()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getWeight(nextVert)
            if nextVert in pq and newDist < nextVert.getDistance():
                # 更新队列中节点的距离和父节点
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.add_task(nextVert, newDist)

def create_graph():
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    return g


graph = create_graph()
start = graph.getVertex(1)
prim(graph, start)
for v in graph:
    print("( %s , %s )" % (v.getId(), v.getPred()))