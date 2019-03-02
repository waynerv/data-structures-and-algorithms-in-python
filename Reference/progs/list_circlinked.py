""" 循环单链表类 """

from list_node import LNode, LinkedListUnderflow


class LCList:  # class of Circular Linked List
    def __init__(self):
        self._rear = None
        
    def is_empty(self):
        return self._rear is None
    
    def prepend(self, elem):  # add element in the front end
        p = LNode(elem)
        if self._rear is None:
            p.next = p  # initiates circle
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
            
    def append(self, elem):  # add element in the rear end
        self.prepend(elem)
        self._rear = self._rear.next
        
    def pop(self):  # pop out head element
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem
    
    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next


if __name__ == '__main__':
    from random import randint

    mlist = LCList()
    for i in range(10):
        mlist.prepend(randint(i, 20))
    for i in range(11, 20):
        mlist.append(randint(i, 30))
    #mlist1.printall()

    while not mlist.is_empty():
        print(mlist.pop())
