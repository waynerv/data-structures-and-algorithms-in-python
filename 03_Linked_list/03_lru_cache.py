import time


class Node(object):
    __slots__ = ('value', 'prev', 'key', 'next')

    def __init__(self, value=None, prev=None, key=None, next=None):
        self.value, self.prev, self.key, self.next = value, prev, key, next


class CircularDoubleLinkedList(object):
    """循环双端链表 ADT
    循环就是把root的prev指向tail节点，串起来
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, node):
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def remove(self, node):
        """remove
        :param node: 传入node 而不是 value 我们就能实现 O(1) 删除
        :return:
        """
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node


class LRUCache(object):
    def __init__(self, maxsize=16):
        self.maxsize = maxsize
        self.cache = {}
        self.access = CircularDoubleLinkedList()
        self.isfull = len(self.cache) >= self.maxsize

    def __call__(self, func):
        def wrapper(n):
            cachenode = self.cache.get(n)
            if cachenode is not None:  # hit
                self.access.remove(cachenode)
                self.access.append(cachenode)
                value = cachenode.value
            else:  # miss
                value = func(n)
                newnode = Node(key=n, value=value)
                self.cache[n] = newnode
                if self.isfull:  # 队列已满
                    lru_node = self.access.headnode()
                    self.access.remove(lru_node)
                    self.access.append(newnode)
                    del self.cache[lru_node.key]
                else:  # 队列未满
                    self.access.append(newnode)
                    self.isfull = len(self.cache) >= self.maxsize
            return value

        return wrapper


@LRUCache()
def fib(n):
    if n <= 2:  # 1 or 2
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def test_lru_cache():
    beg = time.time()
    for i in range(1, 50):
        print(fib(i))
    end = time.time()
    print(end - beg)


if __name__ == '__main__':
    test_lru_cache()
