def lower_bound(array, first, last, value):  # 返回[first, last)内第一个不小于value的值的位置
    while first < last:  # 搜索区间[first, last)不为空
        mid = first + (last - first) // 2  # 防溢出
        if array[mid] < value: # 要找第一个不小于value的值，所以此处应该为小于符号
            first = mid + 1
        else:
            last = mid
    return first  # last也行，因为[first, last)为空的时候它们重合


def test_binary_search():
    a = list(range(10))

    assert lower_bound(a, 0, 10, 3) == 3
    assert lower_bound(a, 0, 10, 10) == 10
    assert lower_bound(a, 0, 10, 9) == 9
    assert lower_bound(a, 0, 10, 0) == 0

    assert lower_bound(a, 0, 10, 9) == 9
