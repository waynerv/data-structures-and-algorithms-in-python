""" 链接表结点类和一个使用结点的简单函数 """

class LinkedListUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


def length(head):
    p, n = head, 0
    while p:
        n += 1
        p = p.next
    return n

if __name__ == '__main__':

    llist1 = LNode(1)
    p = llist1

    for i in range(2, 11):
        p.next = LNode(i)
        p = p.next

    print(length(llist1))

    p = llist1
    while p:
        print(p.elem)
        p = p.next
