""" 图的DFS序列和DFS生成树的函数 
"""

from graph import *

from stack_list import SStack
#from queue_list import SQueue, QueueUnderflow

# Generate the DFS sequence of reachable vertices from v0


def DFS_seq(graph, v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] = 1
    dfs_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i+1, edges))
            if visited[v] == 0:  # unvisited node
                dfs_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return dfs_seq

# Generate span-forest of a graph, recursive definition


def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum

    def dfs(gr, v):
        nonlocal span_forest
        for u, w in gr.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(gr, u)

    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return span_forest


if __name__ == '__main__':
    g1 = GraphAL(gmat1, 0)
    dfs1 = DFS_seq(g1, 0)
    print(dfs1)

    g2 = GraphAL(gmat2, 0)
    dfs2 = DFS_seq(g2, 0)
    print(dfs2, "\n")
    
    dfs_tree = DFS_span_forest(g1)
    print(dfs_tree)
    dfs_tree = DFS_span_forest(g2)
    print(dfs_tree)
