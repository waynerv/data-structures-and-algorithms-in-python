from collections import deque


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def __len__(self):
        return len(self._deque)

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()


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


def BFS(graph, start):
    search_queue = Queue()
    searched = set()
    search_queue.push(start)
    while search_queue:
        cur_node = search_queue.pop()
        if cur_node not in searched:
            print(cur_node)  # or yield cur_node
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)


BFS(graph, 'A')
