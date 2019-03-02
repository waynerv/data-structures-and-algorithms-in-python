""" 单源点最短路径算法，所有顶点对之间的最短路径算法 
"""

from prioqueue import PrioQueue  # , PrioQueueError
from graph import *


# Find nearest pathes from a single vertex to other reachable
# vertices using Dijkstra algorithm, with priority queue.
def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    count, paths = 0, [None]*vnum
    cands = PrioQueue([(0, v0, v0)])
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths


# Find all nearset pathes using Floyd-Warshall algorithm
def all_shortest_paths(graph):
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j) for j in range(vnum)]
         for i in range(vnum)]  # create a copy the adjacent matrix
    nvertex = [[-1 if a[i][j] == inf else j
                for j in range(vnum)]
               for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]
    return a, nvertex


def test_dijkstra():
    paths0 = dijkstra_shortest_paths(g1, 0)
    paths1 = dijkstra_shortest_paths(g1, 1)
    paths2 = dijkstra_shortest_paths(g1, 2)
    paths3 = dijkstra_shortest_paths(g1, 3)
    paths4 = dijkstra_shortest_paths(g1, 4)
    paths5 = dijkstra_shortest_paths(g1, 5)

    if (paths0 != [(0, 0), (3, 41), (0, 10), (2, 25), (0, 45), None] or
        paths1 != [(2, 35), (1, 0), (1, 15), (2, 30), (1, 5), None] or
        paths2 != [(2, 20), (3, 31), (2, 0), (2, 15), (1, 36), None] or
        paths3 != [(2, 51), (3, 16), (1, 31), (3, 0), (1, 21), None] or
        paths4 != [(2, 81), (3, 46), (1, 61), (4, 30), (4, 0), None] or
        paths5 != [(2, 54), (3, 19), (1, 34), (5, 3), (1, 24), (5, 0)]):

        print("Some result are not correct.")

    print("start v0:", paths0)
    print("start v1:", paths1)
    print("start v2:", paths2)
    print("start v3:", paths3)
    print("start v4:", paths4)
    print("start v5:", paths5)
# end test_dijkstra()


def test_floyd():
    paths = all_shortest_paths(g1)
    print("")
    print(paths[0])
    print(paths[1])


if __name__ == '__main__':

    g1 = GraphAL(gmat4, inf)

    test_dijkstra()
    test_floyd()
