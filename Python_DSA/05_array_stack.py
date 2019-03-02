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


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('stack full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('stack empty')
        self.head -= 1
        value = self.array[self.head % self.maxsize]
        return value

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack(5)
    for i in range(5):
        s.push(i)

    assert len(s) == 5
    import pytest
    with pytest.raises(FullError) as excinfo:
        s.push(5)
    assert 'full' in str(excinfo.value)
    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    assert s.is_empty()

    with pytest.raises(Exception) as excinfo:
        s.pop()
    assert 'empty' in str(excinfo.value)
