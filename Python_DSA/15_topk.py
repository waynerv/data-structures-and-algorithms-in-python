import heapq


class TopK(object):
    """获取大量元素 topk 大个元素，固定内存
    思路：
    1. 先放入元素前 k 个建立一个最小堆
    2. 迭代剩余元素：
        如果当前元素小于堆顶元素，跳过该元素（肯定不是前 k 大）
        否则替换堆顶元素为当前元素，并重新调整堆
    """

    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, value):
        if len(self.minheap) >= self.capacity:
            min_value = self.minheap[0]
            if value > min_value:
                heapq.heapreplace(self.minheap, value)  # 返回并且pop堆顶最小值，推入新的 val 值并调整堆
        else:
            heapq.heappush(self.minheap, value)  # 前面 k 个元素直接放入minheap

    def get_topk(self):
        for i in self.iterable:
            self.push(i)
        return self.minheap


def test():
    import random
    mylist = list(range(1000))  # 这里可以是一个可迭代元素，节省内存
    random.shuffle(mylist)
    _ = TopK(mylist, 10)
    print(_.get_topk())


if __name__ == '__main__':
    test()
