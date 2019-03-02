""" 最小生成树的 Prim 算法 
"""

from dec_prioheap import *
from graph import *


def Prim(graph):
    vnum = graph.vertex_num()
    wv_seq = [[graph.get_edge(0, v), v, 0] for v in range(vnum)]
    connects = DecPrioHeap(wv_seq)    # record vertices
    mst = [None]*vnum
    while not connects.is_empty():
        w, mv, u = connects.getmin()  # take nearest vertex and edge
        if w == inf:
            break
        mst[mv] = ((u, mv), w)  # new MST edge and vertex vmin
        for v, w in graph.out_edges(mv):  # edge is in form (v, w)
            if not mst[v] and w < connects.weight(v):
                connects.dec_weight(v, w, mv)
    return mst

if __name__ == '__main__':
    
    pass
