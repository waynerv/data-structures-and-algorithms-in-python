""" 最佳二叉树的实现 
"""

from bintree import BinTNode  # , print_BiTNodes
from assoc import Assoc
from dict_bitree import DictBinTree

inf = float("inf")


class DictOptBinTree(DictBinTree):
    def __init__(self, seq):
        DictBinTree.__init__(self)
        data = sorted(seq)
        self._root = DictOptBinTree.buildOBT(data, 0, len(data)-1)

    @staticmethod
    def buildOBT(data, start, end):
        if start > end:
            return None
        mid = (end + start)//2
        left = DictOptBinTree.buildOBT(data, start, mid-1)
        right = DictOptBinTree.buildOBT(data, mid+1, end)
        return BinTNode(Assoc(*data[mid]), left, right)


def build_opt_btree(wp, wq):
    """ Assume wp is a list of n values representing weights of
internal nodes, wq is a list of n+1 values representing
weights of n+1 external nodes. This function builds the
optimal binary searching tree from wp and wq.
"""
    num = len(wp)+1
    if len(wq) != num:
        raise ValueError("Arguments of build_opt_btree are wrong.")
    w = [[0]*num for j in range(num)]
    c = [[0]*num for j in range(num)]
    r = [[0]*num for j in range(num)]
    for i in range(num):       # 计算所有的 w[i][j]
        w[i][i] = wq[i]
        for j in range(i+1, num):
            w[i][j] = w[i][j-1] + wp[j-1] + wq[j]
    for i in range(0, num-1):  # Set trees with only one node
        c[i][i+1] = w[i][i+1]
        r[i][i+1] = i

    for m in range(2, num):
        # 算 m 个内部结点的最佳树（n–m+1棵）
        for i in range(0, num-m):
            k0, j = i, i+m
            wmin = inf
            for k in range(i, j):
                # 在[i,j)里找使C[i][k]+C[k+1][j]最小的k
                if c[i][k] + c[k+1][j] < wmin:
                    wmin = c[i][k] + c[k+1][j]
                    k0 = k
            c[i][j] = w[i][j] + wmin
            r[i][j] = k0

    return c, r

if __name__ == '__main__':
    # from random import randint

    wp = [5, 1, 2]
    wq = [4, 3, 1, 1]

    trees = build_opt_btree(wp, wq)

    print(trees[0])
    print(trees[1])

    wp = [5, 1, 2, 6, 8, 10]
    wq = [4, 3, 3, 1, 6, 12, 9]

    trees = build_opt_btree(wp, wq)

    print(trees[0])
    print(trees[1])

##    "Result:"
##    [[0, 12, 23, 35, 66, 112, 167],
##     [0,  0,  7, 16, 38,  80, 130],
##     [0,  0,  0,  6, 24,  62, 112],
##     [0,  0,  0,  0, 13,  46,  96],
##     [0,  0,  0,  0,  0,  26,  71],
##     [0,  0,  0,  0,  0,   0,  31],
##     [0,  0,  0,  0,  0,   0,   0]]
##    
##    [[0, 0, 0, 0, 3, 3, 4],
##     [0, 0, 1, 1, 3, 4, 4],
##     [0, 0, 0, 2, 3, 4, 4],
##     [0, 0, 0, 0, 3, 4, 4],
##     [0, 0, 0, 0, 0, 4, 5],
##     [0, 0, 0, 0, 0, 0, 5],
##     [0, 0, 0, 0, 0, 0, 0]]
