""" 单源点最短路径算法，所有顶点对之间的最短路径算法 
"""

from prioqueue import PrioQueue  # , PrioQueueError
from graph import *


# Find nearest pathes from a single vertex to other reachable
# vertices using Dijkstra algorithm.
# Use a loop to find next nearest vertex, time O(V^2), space O(V)
def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert vnum > 0 and 0 <= v0 < vnum
    count, paths = 0, [None]*vnum
    cands = [(inf, v0, i) for i in range(graph.vertex_num())]
    cands[v0] = (0, v0, v0)
    vmin = v0
    while vmin > -1:
        plen = cands[vmin][0]
        paths[vmin] = (cands[vmin][1], plen)
        cands[vmin] = None
        count += 1
        for v, w in graph.out_edges(vmin):
            if cands[v] and plen + w < cands[v][0]:  # Shorter path, update
                cands[v] = (plen + w, vmin, v)
        vmin, plen = -1, inf
        for i in range(vnum):
            if cands[i] and cands[i][0] < plen:
                vmin, plen = i, cands[i][0]
    return paths

# Find nearest pathes from a single vertex to other reachable
# vertices using Dijkstra algorithm.
# Use an priority queue to fine the nearest vertex, time O(E), space O(E)
def dijkstra_shortest_paths_0(graph, v0):
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


def test_dijkstra():
    paths00 = dijkstra_shortest_paths(g1, 0)
    paths01 = dijkstra_shortest_paths_0(g1, 0)
    # paths10 = dijkstra_shortest_paths(g1, 1)
    # paths11 = dijkstra_shortest_paths_0(g1, 1)
    # paths2 = dijkstra_shortest_paths(g1, 2)
    # paths3 = dijkstra_shortest_paths(g1, 3)
    # paths4 = dijkstra_shortest_paths(g1, 4)
    # paths5 = dijkstra_shortest_paths(g1, 5)

    # if (paths0 != [(0, 0), (3, 41), (0, 10), (2, 25), (0, 45), None] or
    #     paths1 != [(2, 35), (1, 0), (1, 15), (2, 30), (1, 5), None] or
    #     paths2 != [(2, 20), (3, 31), (2, 0), (2, 15), (1, 36), None] or
    #     paths3 != [(2, 51), (3, 16), (1, 31), (3, 0), (1, 21), None] or
    #     paths4 != [(2, 81), (3, 46), (1, 61), (4, 30), (4, 0), None] or
    #     paths5 != [(2, 54), (3, 19), (1, 34), (5, 3), (1, 24), (5, 0)]):
    #
    #     print("Some result are not correct.")

    print("start v0:", paths00)
    print("start v0:", paths01)
    # print("start v1:", paths10)
    # print("start v1:", paths11)
    # print("start v4:", paths4)
    # print("start v5:", paths5)
# end test_dijkstra()


if __name__ == '__main__':

    g1 = GraphAL(gmat4, inf)

    test_dijkstra()
