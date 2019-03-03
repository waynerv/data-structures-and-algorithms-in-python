def lower_bound(array, value):  # 返回[first, last)内第一个不小于value的值的位置
    first = 0
    last = len(array)
    while first < last:  # 搜索区间[first, last)不为空
        mid = first + (last - first) // 2  # 防溢出
        if array[mid] < value:
            first = mid + 1
        else:
            last = mid
    return first  # last也行，因为[first, last)为空的时候它们重合


def test_binary_search():
    a = list(range(10))

    assert lower_bound(a, 3) == 3
    assert lower_bound(a, 10) == 10
    assert lower_bound(a, 9) == 9

    assert lower_bound(a, 0) == 0
    assert lower_bound(a, 9) == 9