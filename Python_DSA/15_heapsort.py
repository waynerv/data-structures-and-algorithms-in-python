class Array(object):
    def __init__(self, size=32):  # 关键属性：分配空间和存储单位（使用列表的单个元素作为一个存储单位）
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):  # Called to implement evaluation of self[index]实现下标访问.
        return self._items[index]

    def __setitem__(self, index, value):  # Called to implement assignment to self[index].
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value

        self._count += 1
        self._siftup(self._count - 1)  # 维持堆的特性

    def _siftup(self, ndx):
        if ndx > 0:
            parent = (ndx - 1) // 2
            if self._elements[ndx] > self._elements[parent]:  # 如果插入的值大于 parent，一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]  # 保存 root 值
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下的节点放到root后siftDown
        self._siftdown(0)  # 维持堆特性
        return value

    def _siftdown(self, ndx):
        left = ndx * 2 + 1
        right = (ndx * 2) + 2
        # 找出当前节点及左右子节点中的最大值，与当前节点交换位置，并递归地对换下去的节点执行siftdown操作
        largest = ndx
        if left < self._count and self._elements[left] > self._elements[largest] and \
                self._elements[left] >= self._elements[right]:
            largest = left
        elif right < self._count and self._elements[right] > self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


class MinHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, ndx):
        if ndx > 0:
            parent = (ndx - 1) // 2
            if self._elements[ndx] < self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = (ndx * 2) + 1
        right = (ndx * 2) + 2
        # 找出当前节点及左右子节点中的最小值，与当前节点交换位置，并递归地对换下去的节点执行siftdown操作
        smallest = ndx
        if left < self._count and self._elements[left] < self._elements[smallest] and \
                self._elements[left] <= self._elements[right]:
            smallest = left
        elif right < self._count and self._elements[right] < self._elements[smallest]:
            smallest = right
        if smallest != ndx:
            self._elements[ndx], self._elements[smallest] = self._elements[smallest], self._elements[ndx]
            self._siftdown(smallest)


def heapsort_reverse(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res


def heapsort(array):
    length = len(array)
    minheap = MinHeap(length)
    for i in array:
        minheap.add(i)
    res = []
    for i in range(length):
        res.append(minheap.extract())
    return res


def heapsort_inplace(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    while maxheap._count > 1:
        maxheap._elements[0], maxheap._elements[maxheap._count - 1] = maxheap._elements[maxheap._count - 1], \
                                                                      maxheap._elements[0]
        maxheap._count -= 1
        if maxheap._count == 2:  # 堆中只剩两个元素时直接交换位置，不需要再进行sift操作
            continue
        maxheap._siftdown(0)
    return list(maxheap._elements)


def test_heapsort_reverse():
    import random
    mylist = list(range(10))
    random.shuffle(mylist)
    assert heapsort_reverse(mylist) == sorted(mylist, reverse=True)


def test_heapsort():
    import random
    mylist = list(range(10))
    random.shuffle(mylist)
    assert heapsort(mylist) == sorted(mylist)


def test_heapsort_inplace():
    import random
    mylist = list(range(100))
    random.shuffle(mylist)
    assert heapsort_inplace(mylist) == sorted(mylist)
