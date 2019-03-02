""" 带尾结点引用的单链表类 """

from list_node import LNode, LinkedListUnderflow
from list_linked import LList


class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    # def prepend(self, elem):
    #     self._head = LNode(elem, self._head)
    #     if self._rear is None:  # empty list
    #         self._rear = self._head
            
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:  # empty list
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
            
    def pop_last(self):
        if self._head is None:  # empty list
            raise LinkedListUnderflow("in pop_last of LList1")
        p = self._head
        if p.next is None:  # list with only one element
            e = p.elem
            self._head = None
            self._rear = None
            return e
        while p.next.next:  # till p.next be last node
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


if __name__ == '__main__':
    mlist1 = LList1()
    mlist1.prepend(99)
        
    for i in range(11, 20):
        mlist1.append(i)

    for x in mlist1.filter(lambda y: y % 2 == 0):
        print(x)

    ss = 0
    while not mlist1.is_empty():
        ss += mlist1.pop()
    print(ss)

    for i in range(10):
        mlist1.prepend(i)

    mlist1.printall()
