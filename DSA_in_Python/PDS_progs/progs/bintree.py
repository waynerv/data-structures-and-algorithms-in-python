""" 二叉树结点类和二叉树相关函数，二叉树类等 
"""


class BinTreeNodeError(ValueError):
    pass


class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right
# end of class


def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


def preorder(t, proc):
    if t is None:
        return
    assert(isinstance(t, BinTNode))
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


def inorder(t, proc):
    if t is None:
        return
    inorder(t.left, proc)
    proc(t.data)
    inorder(t.right, proc)


def postorder(t, proc):
    if t is None:
        return
    postorder(t.left, proc)
    postorder(t.right, proc)
    proc(t.data)

from queue_list import *


def levelorder(t, proc):
    q = SQueue()
    q.enqueue(t)
    while not q.is_empty():
        t = q.dequeue()
        if t is None:
            continue
        q.enqueue(t.left)
        q.enqueue(t.right)
        proc(t.data)


from stack_list import *


def preorder_nonrec(t, proc):
    s = SStack()
    while t or not s.is_empty():
        while t:  # go down along left chain
            s.push(t.right)   # push right branch into stack
            proc(t.data)
            t = t.left
        t = s.pop()           # left chain ends, backtrack


# def preorder_nonrec(t, proc):
#     s = SStack()
#     while t:
#         while t:  # go down along left chain
#             if t.right:
#                 s.push(t.right)   # push non-empty right branch into stack
#             proc(t.data)
#             t = t.left
#         if s.is_empty():
#             break
#         t = s.pop()           # left chain ends, backtrack


def inorder_nonrec(t, proc):
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right


def postorder_nonrec(t, proc):
    s = SStack()
    while t or not s.is_empty():
        while t:  # iterate until top has no child
            s.push(t)
            t = t.left if t.left else t.right
            # if we can go left, go, otherwise, go right
        t = s.pop()  # get the node to be access
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right  # end of left visit, turn right
        else:
            t = None  # end of right visit, force to backtrack

def preorder_elements(t):
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()


def print_BinTNodes(t):
    if t is None:
        print("^", end="")
        return
    print("(" + str(t.data), end="")
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")", end="")


class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def preorder_elements(self):
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()


if __name__ == '__main__':
    t1 = BinTNode(1, BinTNode(2, BinTNode(3), BinTNode(4)), BinTNode(5))

    print_BinTNodes(t1)
    print()

    preorder(t1, lambda x: print(x, end=" "))
    print()

    preorder_nonrec(t1, lambda x: print(x, end=" "))
    print()

    inorder(t1, lambda x: print(x, end=" "))
    print()
    

    inorder_nonrec(t1, lambda x: print(x, end=" "))
    print()

    postorder(t1, lambda x: print(x, end=" "))
    print()
    

    postorder_nonrec(t1, lambda x: print(x, end=" "))
    print()

    for x in preorder_elements(t1):
        print(x)
