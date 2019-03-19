import heapq
import itertools


class PriorityQueue(object):
    REMOVED = '<removed-task>'  # 被删除任务的占位字符

    def __init__(self):
        self.pq = []  # 初始化heapq所使用的list
        self.entry_finder = {}  # 任务到优先级条目的映射
        self.counter = itertools.count()  # 唯一计数器

    def add_task(self, task, priority=0):
        """添加一个新任务或者更新一个已存在任务的优先级"""
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        """将一个已存在的任务标记为REMOVED，若未找到Raise KeyError。"""
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

    def pop_task(self):
        """删除并返回最小优先级任务，如果队列已空Raise KeyError"""
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
