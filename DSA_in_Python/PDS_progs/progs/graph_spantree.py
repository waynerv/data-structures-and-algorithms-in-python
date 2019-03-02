""" 最小生成树的 Kruskal 算法 
"""

from prioqueue import PrioQueue  # , PrioQueueError
from graph import *


def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):  # put all edges into a list
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()  # sort, O(n log n) time
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append(((vi, vj), w))
            if len(mst) == vnum-1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst


def Prim(graph):
    """ Assume that graph is a network, a connected undirect
graph. This function implements Prim algorithm to build its
minimal span tree. A list mst to store the resulting
span tree, where each element takes the form ((i, j), w).
A representing array reps is used to record the representive
vertics of each of the connective parts.
"""
    vnum = graph.vertex_num()
    mst = [None]*vnum
    cands = PrioQueue([(0, 0, 0)])    # record cand-edges (w, vi, wj)
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()  # take minimal candidate edge
        if mst[v]:   # vmin is already in mst
            continue
        mst[v] = ((u, v), w)    # record new MST edge and vertex
        count += 1
        for vi, w in graph.out_edges(v):  # for adjacents of vmin
            if not mst[vi]:  # when v is not in mst yet
                cands.enqueue((w, v, vi))
    return mst

inf = float("inf")

if __name__ == '__main__':

    g3 = GraphAL(gmat5, inf)
    g4 = GraphAL(gmat6, inf)

    spt1 = Kruskal(g3)
    print(spt1)

    spt2 = Prim(g3)
    print(spt2)

    spt3 = Kruskal(g4)
    print(spt3)

    spt4 = Prim(g4)
    print(spt4)
