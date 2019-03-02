""" 基于二叉树实现 Huffman 树 
"""

from prioqueue import PrioQueue  # , PrioQueueError
from bintree import BinTNode, print_BinTNodes


class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data


class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)


def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()


if __name__ == '__main__':

    t = BinTNode(1, BinTNode(2), BinTNode(3))
    print_BinTNodes(t)
    print("\n")

    h = HuffmanTree([2, 3, 7, 10, 4, 2, 5])
    print_BinTNodes(h)

    pass
