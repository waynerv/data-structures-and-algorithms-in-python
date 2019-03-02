""" 基于二叉树的字典实现 
"""

from bintree import BinTNode  # , print_BiTNodes
from stack_list import *
from assoc import Assoc
from random import randint


def bt_search(btree, key):
    bt = btree
    while bt:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None


class DictBinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return
    
    def values(self):
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.value
            t = t.right

    def entries(self):
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
            t = t.right

    def delete(self, key):
        p, q = None, self._root  # keep p the parent of q
        while q and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
        if q is None:
            return  # key is not in the tree
        # Now q refers to key node, p is its parent or None
        if q.left is None:    # q has no left child
            if p is None:
                self._root = q.right  # q == self._root
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right     # here q == p.right
            return
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left  # q == self._root
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def print(self):
        for k, v in self.entries():
            print(k, v)
# END class


def build_dictBinTree(entries):
    dic = DictBinTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic


if __name__ == '__main__':
    # from random import randint

    data = [(x, 1) for x in
            [26, 15, 18, 7, 30, 29, 3, 17, 10, 22, 34, 9]]
    dic1 = build_dictBinTree(data)

    for entry in dic1.entries():
        print(entry)

    for i in range(20):
        n = randint(1, 31)
        print("try delete", n, end=", ")
        dic1.delete(n)
    print('')

    for entry in dic1.entries():
        print(entry)

    pass

