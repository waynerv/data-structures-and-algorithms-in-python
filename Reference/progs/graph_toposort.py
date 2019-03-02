""" 有向图的拓扑排序算法 
"""

from graph import *


# We suppose that A[i][i] = unconn value
def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0]*vnum, []
    zerov = -1
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            indegree[v] += 1
    for vi in range(vnum):
        if indegree[vi] == 0:
            indegree[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1:  # There is no topo-seq
            return False
        toposeq.append(zerov)
        vi = zerov
        zerov = indegree[zerov]
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq

""" generate critical path of AOE 
"""


# graph 里无边用 inf 表示
def critical_path(graph):
    toposeq = toposort(graph)
    if not toposeq:  # no topo-sequence, cannot continue
        return False
    vnum = graph.vertex_num()
    crt_actions = []
    ee = event_earliest_time(vnum, graph, toposeq)
    le = event_latest_time(vnum, graph, toposeq, ee[vnum-1])
    for i in range(vnum):
        for j, w in graph.out_edges(i):
            if ee[i] == le[j] - w:  # a critical action
                crt_actions.append([i, j, ee[i]])
    return crt_actions  # return the critical actions


def event_earliest_time(vnum, graph, toposeq):
    ee = [0]*vnum
    for k in range(vnum-1):        # 最后一个顶点不必做
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if ee[i] + w > ee[j]:  # 事件 j 还更晚结束?
                ee[j] = ee[i] + w
    return ee


def event_latest_time(vnum, graph, toposeq, eelast):
    le = [eelast]*vnum
    for k in range(vnum-2, -1, -1):  # 逆拓扑顺序, 两端顶点都不必做
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if le[j] - w < le[i]:    # 事件 i 应更早开始?
                le[i] = le[j] - w
    return le


def critical_paths(graph):
    def events_earliest_time(vnum, graph, toposeq):
        ee = [0]*vnum
        for i in toposeq:
            for j, w in graph.out_edges(i):
                if ee[i] + w > ee[j]:  # 事件j还更晚结束?
                    ee[j] = ee[i] + w
        return ee

    def event_latest_time(vnum, graph, toposeq, eelast):
        le = [eelast]*vnum
        for k in range(vnum-2, -1, -1):  # 逆拓扑顺序
            i = toposeq[k]
            for j, w in graph.out_edges(i):
                if le[j] - w < le[i]:    # 事件i应更早开始?
                    le[i] = le[j] - w
        return le

    def crt_paths(vnum, graph, ee, le):
        crt_actions = []
        for i in range(vnum):
            for j, w in graph.out_edges(i):
                if ee[i] == le[j] - w:   # 关键活动
                    crt_actions.append((i, j, ee[i]))
        return crt_actions
    
    toposeq = toposort(graph)
    if not toposeq:  # 没有拓扑序列，失败结束
        return False
    vnum = graph.vertex_num()
    ee = events_earliest_time(vnum, graph, toposeq)
    le = event_latest_time(vnum, graph, toposeq, ee[vnum-1])
    return crt_paths(vnum, graph, ee, le)


if __name__ == '__main__':


    g7 = GraphAL(gmat7)


    g8 = GraphAL(gmat8, inf)

##    toposeq = toposort(g7)
##    print(toposeq)

    cp = critical_path(g8)
    print(cp)
    cp = critical_paths(g8)
    print(cp)
    
    pass
