from collections import deque


class Stack:
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def __len__(self):
        return len(self._deque)

    def is_empty(self):
        return len(self._deque) == 0


graph = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}

DFS_searched = set()


def DFS_recursive(graph, start):
    if start not in DFS_searched:
        print(start)
        DFS_searched.add(start)
    for node in graph[start]:
        if node not in DFS_searched:
            DFS_recursive(graph, node)


print('dfs recursive:')
DFS_recursive(graph, 'A')


def DFS(graph, start):
    s = Stack()
    s.push(start)
    searched = set()
    while not s.is_empty():
        cur_node = s.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in reversed(graph[cur_node]):  # 注意入栈出栈的顺序
                s.push(node)


print('dfs use stack:')
DFS(graph, 'A')
