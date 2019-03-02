""" 基于链接表概念（链接结点）实现的栈类 """

from list_node import LNode


class StackUnderflow(ValueError):
    pass


class LStack():  # stack implemented as a linked node list
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow
        e = self._top.elem
        self._top = self._top.next
        return e


if __name__ == '__main__':
    from random import randint
    st1 = LStack()

    for i in range(10):
        st1.push(randint(1, 20))

    print(st1.pop())
    st1.pop()
    st1.push(20)
    st1.push(100)
    while not st1.is_empty():
        print(st1.pop())
