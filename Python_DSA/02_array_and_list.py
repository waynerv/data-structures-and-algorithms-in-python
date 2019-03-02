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


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10
