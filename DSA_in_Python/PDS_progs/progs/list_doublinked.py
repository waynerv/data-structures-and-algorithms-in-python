""" 双链表结点类，带尾结点引用的双链表类 """

from list_node import LNode, LinkedListUnderflow
from list_linked1 import LList1


class DLNode(LNode):  # class of Double Linked Nodes
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


class DLList(LList1):  # class of Double Linked List
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:  # otherwise, create the prev reference
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:  # insert in empty list
            self._head = p
        else:  # otherwise, create the next reference
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of LDList")
        e = self._head.elem
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of LDList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None  # it is empty now
        else:
            self._rear.next = None
        return e

if __name__ == '__main__':
    from random import randint
    mlist = DLList()
    for i in range(10):
        mlist.prepend(randint(i, 30))
    for i in range(11, 20):
        mlist.append(randint(1, 50))

    mlist.printall()

    for x in mlist.filter(lambda y: y % 2 == 1):
        print(x)

    while not mlist.is_empty():
        print(mlist.pop())
        if not mlist.is_empty():
            print(mlist.pop_last())
