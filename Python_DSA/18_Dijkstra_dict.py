nodes = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisted = {node:float('inf') for node in nodes}
visted = {}
current = 'B'
currentDistance = 0
unvisted[current] = currentDistance

while True:
    for neighbor, weight in nodes[current].items():
        if neighbor not in unvisted:
            continue
        newDistance = currentDistance + weight
        if newDistance < unvisted[neighbor]:
            unvisted[neighbor] = newDistance
    # 将当前节点加入已确定最短距离集合
    visted[current] = currentDistance
    del unvisted[current]
    if not unvisted:
        break
    # 从未遍历的节点集合中选出距离最小的节点
    candidates = [node for node in unvisted.items()]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visted)