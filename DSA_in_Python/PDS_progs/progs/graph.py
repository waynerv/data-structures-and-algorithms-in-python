""" 基本的图实现：邻接矩阵实现，链接表实现 
"""

inf = float("inf")  # 表示无穷大


class GraphError(TypeError):
    pass


class Graph:  # basic graph class, using adjacent matrix
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError("Argument for class 'Graph' is bad.")
        self._mat = [mat[i][:] for i in range(vnum)]  # 做 mat 的拷贝
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise GraphError(
            "Adj-Matrix does not support 'add_vertex'.")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex.")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex.")
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    # @staticmethod
    # def _out_edges(row, unconn):
    #     for i in range(len(row)):
    #         if row[i] != unconn:
    #             yield (i, row[i])

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]"\
               + "\nUnconnected: " + str(self._unconn)


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否方阵
                raise ValueError("Argument for 'GraphA' is bad.")
        self._mat = [Graph._out_edges(mat[i], unconn)
                     for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):  # 增加新顶点时安排一个新编号
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge into empty graph.")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex.")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:  # 修改 mat[vi][vj] 的值
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:  # 原无到vj的边，退出循环在正确位置加入
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex.")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._mat[vi]


gmat = [[0, 0, 3, 4],
        [2, 0, 0, 0],
        [4, 1, 0, 0],
        [2, 0, 1, 0]]

gmat1 = [[0,1,1,0,0,0,0,0],
         [1,0,0,1,1,0,0,0],
         [1,0,0,0,0,1,1,0],
         [0,1,0,0,0,0,0,1],
         [0,1,0,0,0,0,0,1],
         [0,0,1,0,0,0,0,0],
         [0,0,1,0,0,0,0,0],
         [0,0,0,1,1,0,0,0]]

gmat2 = [[0,1,0,1,1,1,0],
         [0,0,1,0,0,0,0],
         [0,0,0,0,0,1,0],
         [0,0,1,0,0,0,0],
         [0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0],
         [0,0,1,0,0,1,0]]

gmat4 = [[  0, 50, 10,inf, 45,inf],
         [inf,  0, 15,inf,  5,inf],
         [ 20,inf,  0, 15,inf,inf],
         [inf, 16,inf,  0, 35,inf],
         [inf,inf,inf, 30,  0,inf],
         [inf,inf,inf,  3,inf,  0]]

gmat5 = [[  0, 10,inf,inf, 19, 21],
         [ 10,  0,  5,  6,inf, 11],
         [inf,  5,  0,  6,inf,inf],
         [inf,  6,  6,  0, 18, 14],
         [ 19,inf,inf, 18,  0,  7],
         [ 21, 11,inf, 14,  7, 0]]

gmat6 = [[  0, 10,inf,inf, 19, 21],
         [ 10,  0,  5,  6,inf, 11],
         [inf,  5,  0,  6,inf,inf],
         [inf,  6,  6,  0, 18, 14],
         [ 19,inf,inf, 18,  0, 33],
         [ 21, 11,inf, 14, 33,  0]]

gmat7 = [[0,0,1,0,0,0,0,1,0],
         [0,0,1,1,1,0,0,0,0],
         [0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,1,1,0,0],
         [0,0,0,0,0,1,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,1,0,0]]

gmat8 = [[inf,  6,  4,  5,inf,inf,inf,inf,inf],
         [inf,inf,inf,inf,  1,inf,inf,inf,inf],
         [inf,inf,inf,inf,  1,inf,inf,inf,inf],
         [inf,inf,inf,inf,inf,  2,inf,inf,inf],
         [inf,inf,inf,inf,inf,inf,  9,  7,inf],
         [inf,inf,inf,inf,inf,inf,inf,  4,inf],
         [inf,inf,inf,inf,inf,inf,inf,inf,  2],
         [inf,inf,inf,inf,inf,inf,inf,inf,  4],
         [inf,inf,inf,inf,inf,inf,inf,inf,inf]]


if __name__ == '__main__':


#    g1 = Graph(gmat, 0)
#    print(str(g1), '\n')

    g3 = GraphAL(gmat, 0)
    print(str(g3))
    g3.add_edge(0, 3, 5)
    g3.add_edge(1, 3, 6)
    g3.add_edge(3, 1, 9)
    x = g3.add_vertex()
    print(x)
    g3.add_edge(x, 1, 5)
    g3.add_edge(2, x, 6)
    print(str(g3))
