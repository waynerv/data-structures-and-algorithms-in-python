""" 链接表类，其中使用链接表结点类 """

from list_node import LNode, LinkedListUnderflow


class LList:
    def __init__(self):
        self._head = None
        
    def is_empty(self):
        return self._head is None
    
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
    
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:  # empty list
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:  # list with only one element
            e = p.elem
            self._head = None
            return e
        while p.next.next:  # till p.next be last node
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p:
            print(p.elem, end='')
            if p.next:
                print(', ', end='')
            p = p.next
        print('')

    def rev(self):
        p = None
        while self._head:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return

        rem = p.next
        p.next = None
        while rem:
            p = self._head
            q = None
            while p and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p

    # def sort(self):
    #     if self.head is None:
    #         return
    #     last = self.head
    #     crt = last.next  # 初始，排序段只有一个结点
    #     while crt:  # 循环，一次处理一个结点
    #         p = self.head
    #         q = None  # 设置扫描指针初值
    #         while p is not crt and p.elem <= crt.elem:
    #             q = p
    #             p = p.next  # 顺序更新两个扫描指针
    #         if p is crt:  # p 是 crt 时不用修改链接，设置 last 到下一结点 crt
    #             last = crt
    #         else:
    #             last.next = crt.next  # 取下当前结点
    #             crt.next = p  # 接好后链接
    #             if q is None:
    #                 self.head = crt  # 作为新的首结点
    #             else:
    #                 q.next = crt  # 或者接在表中间
    #         crt = last.next  # 无论什么情况，crt 总是 last 的下一结点

    def for_each(self, proc):
        p = self._head
        while p:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p:
            yield p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                yield p.elem
            p = p.next

#end of class LList


def list_sort(lst):
    for i in range(1, len(lst)):  # seg [0:0] is sorted
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:  # moving one by one
            lst[j] = lst[j-1]          # in reversed-order
            j -= 1
        lst[j] = x


import random

if __name__ == '__main__':
    mlist1 = LList()

    for i in range(10):
        mlist1.prepend(i)

    for i in range(11, 20):
        mlist1.append(i)

    mlist1.printall()
    for i in range(5):
        print(mlist1.pop())
        print(mlist1.pop_last())

    print('remained:')
    mlist1.printall()
    mlist1.rev()
    print('\nreversed:')
    mlist1.printall()

    mlist1.sort()
    print('\nsorted:')
    mlist1.printall()
    for x in mlist1.elements():
        print(x)
    print('\n')

    list1 = [random.randint(1, 50) for i in range(20)]
    print(list1, '\n')
    list_sort(list1)
    print(list1)
