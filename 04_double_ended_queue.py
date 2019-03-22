class Node(object):
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


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

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:  # 先看看插入的链表是否已满
            raise Exception('LinkedList is full.')
        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is full.')
        node = Node(value=value)

        headnode = self.headnode()
        self.root.next = node
        node.prev = self.root
        node.next = headnode
        headnode.prev = node
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

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """相比单链表独有的反序遍历"""
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


class DoubleEndedQueue(CircularDoubleLinkedList):

    def pop(self):
        if self.tailnode() is self.root:
            raise Exception('LinkedList is empty.')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if self.headnode() is self.root:
            raise Exception('LinkedList is empty.')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


def test_double_ended_queue():
    mydeque = DoubleEndedQueue()
    assert len(mydeque) == 0

    mydeque.appendleft(0)
    assert list(mydeque) == [0]
    assert len(mydeque) == 1
    assert mydeque.root.next is not mydeque.root
    headnode = mydeque.headnode()
    assert headnode.value == 0
    mydeque.remove(headnode)
    assert len(mydeque) == 0
    mydeque.append(0)
    mydeque.append(1)
    mydeque.append(2)

    assert list(mydeque) == [0, 1, 2]

    assert [node.value for node in mydeque.iter_node()] == [0, 1, 2]
    assert [node.value for node in mydeque.iter_node_reverse()] == [2, 1, 0]

    headnode = mydeque.headnode()
    assert headnode.value == 0
    mydeque.remove(headnode)
    assert len(mydeque) == 2
    assert [node.value for node in mydeque.iter_node()] == [1, 2]

    mydeque.appendleft(0)
    assert [node.value for node in mydeque.iter_node()] == [0, 1, 2]

    mydeque.append(3)
    mydeque.pop()
    assert [node.value for node in mydeque.iter_node()] == [0, 1, 2]
    mydeque.popleft()
    assert [node.value for node in mydeque.iter_node()] == [1, 2]
