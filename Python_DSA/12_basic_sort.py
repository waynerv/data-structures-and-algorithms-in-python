import random


def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):  # 需要减去i是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)
    assert seq == sorted(seq)


def selection_sort(seq):
    n = len(seq)
    for i in range(n - 1): 
        min_index = i  # 假设当前下标的元素是最小的
        for j in range(i + 1, n):  # 从i之后开始找到最小的元素，一直找到最后一个元素
            if seq[j] < seq[min_index]:
                min_index = j  # 循环结束后得到最小元素的下标
        if min_index != i:  # 如果最小的元素不是当前下标的元素，则交换位置
            seq[i], seq[min_index] = seq[min_index], seq[i]


def test_selection_sort():
    seq = list(range(10))
    random.shuffle(seq)
    selection_sort(seq)
    assert seq == sorted(seq)


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):  # 从第二个元素开始遍历
        value = seq[i]  # 取出当前位置元素的值
        pos = i  # 找到这个值的合适位置，使得前边的数组有序 [0,i] 有序
        while pos > 0 and value < seq[pos - 1]:  # 比较取出值与前面的元素值，如果取出值跟小，继续前移
            seq[pos] = seq[pos - 1]  # 将比较过的值往后移
            pos -= 1  # 继续往前比较（前移取出值的位置）
        seq[pos] = value  # 将取出的值插入到当前位置


def test_insertion_sort():
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort(seq)
    assert seq == sorted(seq)
