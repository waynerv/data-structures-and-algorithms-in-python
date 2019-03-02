""" 排序算法
"""

from random import randrange


class Record:
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum

    def __str__(self):
        return "R("+str(self.key)+", "+str(self.datum)+")"


def printR(lst):
    print("["+", ".join(map(str, lst))+"]")


#### 简单插入排序
##def insert_sort(lst) :
##    for i in range(1, len(lst)): # 开始时片段[0:1]已排序
##        x = lst[i]
##        j = i
##        while j > 0 and lst[j-1].key > x.key:
##            lst[j] = lst[j-1]  # 反序逐个后移元素至确定插入位置
##            j -= 1
##        lst[j] = x
##
##
##def test1(n):
##    l1 = [Record(randint(1, 20), i) for i in range(n)]
##    printR(l1)
##    insert_sort(l1)
##    printR(l1)


#### 简单选择排序
##def select_sort(lst):
##    for i in range(len(lst)-1):
##        k = i
##        for j in range(i, len(lst)):
##            if lst[j].key < lst[k].key:
##                k = j
##        if i != k:
##            lst[i], lst[k] = lst[k], lst[i]
##
##
##def test2(n):
##    l1 = [Record(randint(1, 20), i) for i in range(n)]
##    printR(l1)
##    select_sort(l1)
##    printR(l1)


#### 简单起泡排序
##def bubble_sort(lst):
##    for i in range(len(lst)):
##        for j in range(1, len(lst)-i):
##            if lst[j-1].key > lst[j].key:
##                lst[j-1], lst[j] = lst[j], lst[j-1]


#### 起泡排序，无逆序时提前结束
##def bubble_sort(lst):
##    for i in range(len(lst)):
##        found = False
##        for j in range(1, len(lst)-i):
##            if lst[j-1].key > lst[j].key:
##                lst[j-1], lst[j] = lst[j], lst[j-1]
##                found = True
##        if not found:
##            break
##
##
##def test3(n):
##    l1 = [Record(randint(1, 20), i) for i in range(n)]
##    printR(l1)
##    bubble_sort(l1)
##    printR(l1)


#### 快速排序
##def quick_sort(lst):
##    def qsort_rec(lst, l, r):
##        if l >= r:
##            return      # 分段中无记录或只有一个记录
##        i, j = l, r
##        pivot = lst[i]
##        while i < j:    # 找 pivot 的最终位置
##            while i < j and lst[j].key >= pivot.key:
##                j -= 1  # 用 j 向左找小于 pivot 的记录移到左边
##            if i < j:
##                lst[i] = lst[j]
##                i += 1
##            while i < j and lst[i].key <= pivot.key:
##                i += 1  # 用 i 向右找大于 pivot 的记录移到右边
##            if i < j:
##                lst[j] = lst[i]
##                j -= 1
##        lst[i] = pivot          # 将 pivot 存入其最终位置
##        qsort_rec(lst, l, i-1)  # 递归处理左半区间
##        qsort_rec(lst, i+1, r)  # 递归处理右半区间
##
##    qsort_rec(lst, 0, len(lst)-1)  # 主函数调用 qsort_rec
##
##
##def test4(n):
##    l1 = [Record(randint(1, 20), i) for i in range(n)]
##    printR(l1)
##    quick_sort1(l1)
##    printR(l1)


#### 快速排序的另一种实现
##def quick_sort1(lst):
##    def qsort(lst, begin, end):
##        if begin >= end:
##            return
##        pivot = lst[begin].key
##        i = begin
##        for j in range(begin + 1, end + 1):
##            if lst[j].key < pivot: # 发现一个小元素
##                i += 1
##                lst[i], lst[j] = lst[j], lst[i] # 小元素交换到前面
##        lst[begin], lst[i] = lst[i], lst[begin] # 枢轴元素就位
##        qsort(lst, begin, i - 1)
##        qsort(lst, i + 1, end)
##
##    qsort(lst, 0, len(lst) - 1)
##
##
##def test4(n):
##    l1 = [Record(randint(1, 20), i) for i in range(n)]
##    printR(l1)
##    quick_sort1(l1)
##    printR(l1)


#### 归并排序
##def merge_sort(lst):
##    slen, llen = 1, len(lst)
##    templst = [None] * llen
##    while slen <= llen:
##        merge_pass(lst, templst, llen, slen)
##        slen *= 2
##        merge_pass(templst, lst, llen, slen)  # 结果存回原位
##        slen *= 2
##
##
##def merge_pass(lfrom, lto, llen, slen):
##    i = 0
##    while i + 2 * slen < llen:  # 归并长slen的两段
##        merge(lfrom, lto, i, i + slen, i + 2 * slen)
##        i += 2 * slen
##    if i + slen < llen:  # 剩下两段，后段长度小于slen
##        merge(lfrom, lto, i, i + slen, llen)
##    else:   # 只剩下一段，复制到表lto
##        for j in range(i, llen):
##            lto[j] = lfrom[j]
##
##
##def merge(lfrom, lto, low, m, high):
##    i, j, k = low, m, low
##    while i < m and j < high:  # 反复复制两段首记录中较小的
##        if lfrom[i].key <= lfrom[j].key:
##            lto[k] = lfrom[i]
##            i += 1
##        else:
##            lto[k] = lfrom[j]
##            j += 1
##        k += 1
##    while i < m:     # 复制第一段剩余记录
##        lto[k] = lfrom[i]
##        i += 1
##        k += 1
##    while j < high:  # 复制第二段剩余记录
##        lto[k] = lfrom[j]
##        j += 1
##        k += 1
##
##
##def test5(n):
##    l1 = [Record(randint(1, 20), i) for i in range(n)]
##    printR(l1)
##    merge_sort(l1)
##    printR(l1)


#### 基数排序
#### 假设被排序仍是以记录类型 Record 为元素的表，其中
####   关键码是数字 0 到 9 的序列（元组），长度 r 为参数
#### 排序中用 10 个 list 存储各关键码元素对应的序列
#### 一遍分配后收集回到原表，r 遍分配和收集完成排序工作

def radix_sort(lst, r):
    rlists = [[] for i in range(10)]
    llen = len(lst)
    for d in range(-1, -r-1, -1):
        for j in range(llen):
            rlists[lst[j].key[d]].append(lst[j])
        j = 0
        for i in range(10):
            tmp = rlists[i]
            for k in range(len(tmp)):
                lst[j] = tmp[k]
                j += 1
            rlists[i].clear()


def test6(n):
    lst = [Record(tuple((randrange(10) for j in range(3))),
                  i) for i in range(n)]
    printR(lst)
    radix_sort(lst, 3)
    printR(lst)
    print()
    
        
            
    






if __name__ == '__main__':
    test6(15)

    test6(19)
