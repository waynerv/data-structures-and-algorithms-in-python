""" AVL 树实现 
"""

from bintree import BinTNode  # , print_BiTNodes
# from stack_list import *
from assoc import Assoc
from dict_bitree import DictBinTree


class AVLNode(BinTNode):
    def __init__(self, data):
        BinTNode.__init__(self, data)
        self.bf = 0        


class DictAVL(DictBinTree):
    def __init__(self):
        DictBinTree.__init__(self)

    @staticmethod
    def LL(a, b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def RR(a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        c = b.right
        a.left, b.right = c.right, c.left 
        c.left, c.right = b, a
        if c.bf == 0:    # c 本身就是插入结点
            a.bf = b.bf = 0 
        elif c.bf == 1:  # 新结点在 c 左子树
            a.bf = -1
            b.bf = 0
        else:            # 新结点在 c 右子树
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:    # c 本身就是插入结点
            a.bf = 0
            b.bf = 0
        elif c.bf == 1:  # 新结点在 c 的左子树
            a.bf = 0
            b.bf = -1
        else:            # 新结点在 c 的右子树
            a.bf = 1
            b.bf = 0
        c.bf = 0 
        return c

    def insert(self, key, value):
        a = p = self._root
        if a is None:
            self._root = AVLNode(Assoc(key, value))
            return
        pa = q = None  # 维持 pa, q 为 a, p 的父结点
        while p:       # 确定插入位置及最小非平衡子树
            if key == p.data.key:  # key存在，修改关联值
                p.data.value = value
                return
            if p.bf != 0:
                pa, a = q, p  # 已知最小非平衡子树
            q = p
            if key < p.data.key:
                p = p.left
            else:
                p = p.right
        # q 是插入点的父结点，parent，a 记录最小非平衡子树
        node = AVLNode(Assoc(key, value))
        if key < q.data.key:
            q.left = node   # 作为左子结点
        else:
            q.right = node  # 或右子结点
        # 新结点已插入，a 是最小不平衡子树
        if key < a.data.key:  # 新结点在 a 的左子树
            p = b = a.left
            d = 1
        else:                # 新结点在 a 的右子树
            p = b = a.right
            d = -1   # d记录新结点在a哪棵子树
        # 修改 b 到新结点路上各结点的BF值，b 为 a 的子结点
        while p != node:     # node 一定存在，不用判断 p 空
            if key < p.data.key:   # p 的左子树增高
                p.bf = 1
                p = p.left
            else:                  # p的右子树增高
                p.bf = -1
                p = p.right
        if a.bf == 0:   # a原BF为0，不会失衡
            a.bf = d
            return
        if a.bf == -d:  # 新结点在较低子树里
            a.bf = 0
            return
        # 新结点在较高子树，失衡，必须调整
        if d == 1:       # 新结点在 a 的左子树
            if b.bf == 1:
                b = DictAVL.LL(a, b)  # LL 调整
            else:
                b = DictAVL.LR(a, b)  # LR 调整
        else:            # 新结点在 a 的右子树
            if b.bf == -1:
                b = DictAVL.RR(a, b)  # RR 调整
            else:
                b = DictAVL.RL(a, b)  # RL 调整

        if pa is None:
            self._root = b    # 原 a 为树根
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b
    
    def delete(self, key):
        return

    def print(self):
        for entry in self.entries():
            print(entry.key, entry.value)

    def depth(self):
        def depth0(t):
            if t is None:
                return 0
            return max(depth0(t.left),
                       depth0(t.right)) + 1
        return depth0(self._root)
        
# END class


def build_AVLTree(entries):
    dic = DictAVL()
    for k, v in entries:
        dic.insert(k, v)
    return dic


def build_random_AVL(n):
    dic = DictAVL()
    for i in range(n):
        dic.insert(randint(1, n*2), randint(1, 100))
    return dic


if __name__ == '__main__':
    from random import randint
    
##    dic1 = build_random_AVL(20)
##    for entry in dic1.inorder():
##        print(entry.key, entry.value)

    dic2 = DictAVL()
    for i in range(15):  # 15 entries with increasing keys
        dic2.insert(i, i*i)
    print(dic2.depth())
    for entry in dic2.entries():
        print(entry.key, entry.value)

##    dic3 = build_random_AVL(1000)
##    print(dic3.depth())
##
##    dic4 = DictAVL()
##    for i in range(1000): # 1000 entries with increasing keys
##        dic4.insert(i, i*i)
##    print(dic4.depth())
    

    pass
