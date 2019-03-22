def shell_sort(seq):
    n = len(seq)
    group = 2  # 每次将序列分成n/2^i个子序列（i从1开始递增）
    gap = n // group  # 子序列数量，同时也是下标增量值
    while gap > 0:  # 增量值最终递减到1
        # 对每个子序列进行插入排序,共进行gap轮
        for i in range(gap):
            # 对当前序列进行插入排序，从当前序列的第二个元素即i+gap开始比较（初始元素下标为i）
            for j in range(i + gap, n, gap):  # 以gap为step获取遍历序列
                value = seq[j]
                pos = j

                while pos >= gap and value < seq[pos - gap]:  # pos-gap>=0,因此pos>=gap
                    seq[pos] = seq[pos - gap]
                    pos -= gap

                seq[pos] = value
        gap = gap // group


def test_insertion_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    shell_sort(seq)
    assert seq == sorted(seq)
