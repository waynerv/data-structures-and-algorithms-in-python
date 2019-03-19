"""
本解法只适用于有向无环图
仅用于理解算法思想，时间复杂度和空间复杂度都很辣鸡
"""

graph = {
    'A': {'B': 6, 'C': 2},
    'B': {'D': 1},
    'C': {'B': 3, 'D': 5},
    'D': {},
}

costs = {
    'B': 6,
    'C': 2,
    'D': float('inf')
}

parents = {
    'B': 'A',
    'C': 'A',
    'D': None
}

processed = set()


def find_lowest_cost_node(costs):
    """
    遍历所有节点，找出未处理过的节点中开销最小的节点
    :param costs:
    :return:
    """
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # 比较开销，找出最小开销节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)  # 在未处理的节点中找到开销最小的节点
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]: # 如果经当前节点前往该邻居更近
            costs[n] = new_cost  # 更新该邻居的开销
            parents[n] = node  # 同时更新该邻居的父亲节点为当前节点
    processed.add(node)  # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环

print(parents.items())
