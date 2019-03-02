""" 字符串匹配算法 """

# Naive string matching


def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:  # i==m means a matching
        if p[i] == t[j]:    # ok! consider next char in p
            i, j = i + 1, j + 1
        else:               # no! consider next position in t
            i, j = 0, j - i + 1
    if i == m:  # find a matching, return its index
        return j - i
    return -1   # no matching, return special value


## KMP string matching


def gen_pnext0(p):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:    # generate pnext[i+1]
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            pnext[i] = k  # set a pnext entry
        else:
            k = pnext[k]
    return pnext


def gen_pnext(p):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法,
    有稍许修改的优化版本.
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:  # 生成下一个pnext元素
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            if p[i] == p[k] :
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def matching_KMP(t, p, pnext):
    """ KMP字符串匹配, 主函数."""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:  # i==m说明找到匹配
        if i == -1 or t[j] == p[i]:  # 考虑p中下一字符
            j, i = j+1, i+1
        else:               # 失败! 考虑由pnext确定的字符
            i = pnext[i]
    if i == m:     # 找到匹配, 返回其下标
        return j-i
    return -1      # 不存在匹配, 返回特殊值


def KMP_matching(t, p):
    """ KMP字符串匹配的另一个版本, 稍许修改（非本质）.
    将gen_pnext定义为局部函数.
    """
    def gen_pnext(p):
        """生成p中各i的下一检查位置表，稍许优化版本."""
        i, k, m = 0, -1, len(p)
        pnext = [-1] * m
        while i < m-1:  # generate pnext[i+1]
            if k == -1 or p[i] == p[k]:
                i, k = i+1, k+1
                if p[i] == p[k] :
                    pnext[i] = pnext[k]
                else:
                    pnext[i] = k
            else:
                k = pnext[k]
        return pnext

    j, i = 0, 0
    n, m = len(t), len(p)
    pnext = gen_pnext(p)
    while j < n and i < m:  # i==m means a matching
        while i >= 0 and t[j] != p[i]:
            i = pnext[i]
        j, i = j+1, i+1
    if i == m:  # 找到匹配, 返回其下标
        return j-i
    return -1   # 不存在匹配, 返回特殊值


def matching(t, p):
    return matching_KMP(t, p, gen_pnext0(p))

t = "aabababababbbbaababaaaababababbab"
p = "abbab"

t1 = "aabcbabcaabcabcaababcabbcaab"
p1 = "abcaababc"

p2 = "abcabcaaa"
t2 = "abcabcaababcaababcabbabbcabcabcaaabccabccab"
