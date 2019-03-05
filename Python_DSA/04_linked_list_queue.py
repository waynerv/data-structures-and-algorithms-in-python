class Node(object):
    __slots__ = ('value', 'next')

    def __init__(self, value=None, next=None):  # 定义链表中的单个节点
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """链接表 ADT
    [ROOT] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """链表的关键属性：可用空间，根节点，尾节点指针，长度
        :param maxsize: int or None, 如果是 None，链表可用空间可无限扩充
        """
        self.maxsize = maxsize
        self.root = Node()  # 默认 root 节点指向 None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:  # 先看看插入的链表是否已满
            raise Exception('LinkedList is Full')
        node = Node(value)  # 构造节点
        tailnode = self.tailnode
        if tailnode is None:  # 检查链表是否为空，即没有插入过新节点
            self.root.next = node  # # 还没有 append 过，length = 0， 追加到 root 后
        else:  # 否则追加到最后一个节点的后边，并更新最后一个节点是 append 的节点
            tailnode.next = node
        self.tailnode = node  # 更新尾节点指向append的节点
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:  # 如果原链表为空，插入第一个元素需要设置 tailnode
            self.tailnode = node

        headnode = self.root.next  # 考虑原链表为空或不为空两种情况，执行代码相同
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
        curnode = self.root.next  # 从第一个节点开始遍历
        while curnode is not self.tailnode:  # 当前遍历节点为尾节点时终止循环
            yield curnode
            curnode = curnode.next  # 移动到下一个节点
        if curnode is not None:
            yield curnode  # yield当前遍历到的节点

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        """删除包含值的一个节点，将其前一个节点的next指向被查询节点的下一个节点即可

        :param value: 要删除的值
        :return: 1或-1，表明删除操作是否成功
        """
        prevnode = self.root  # 需要设置变量记住要删除节点的上一个节点，初始值为根节点
        for curnode in self.iter_node():  # 遍历查找等于value值的节点
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:  # NOTE: 注意更新 tailnode
                    if prevnode is self.root:
                        self.tailnode = None  # 当前一个节点为根节点时，仍将尾节点指向None
                    else:
                        self.tailnode = prevnode  # 否则指向前一个节点即可
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:
                prevnode = curnode
        return -1  # 表明删除失败

    def find(self, value):  # O(n)
        """查找一个节点，返回序号，从0开始

        :param value: 查找的值
        """
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1  # 没找到

    def popleft(self):
        """删除第一个链表节点
        """
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:  # 单节点删除 tailnode 的处理
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None


########################################
# Queue的实现
########################################
class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:  # 注意判断队列是否已满
            raise FullError('queue full')
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:  # 注意判断队列是否为空
            raise EmptyError('queue empty')
        return self._item_linked_list.popleft()


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        q.pop()
    assert 'queue empty' == str(excinfo.value)