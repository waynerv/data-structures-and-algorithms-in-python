def binary_search(sorted_list, beg, end, value):  # 双闭区间, end=len(a)-1
    if not sorted_list:
        return -1

    while beg <= end:
        mid = (beg + end) // 2
        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] < value:
            beg = mid + 1
        else:
            end = mid - 1
    return -1


def test_binary_search():
    a = list(range(10))

    assert binary_search(a, 0, len(a) - 1, 3) == 3
    assert binary_search(a, 0, len(a) - 1, 10) == -1
    assert binary_search(a, 0, len(a) - 1, 9) == 9

    assert binary_search(None, 0, len(a) - 1, 0) == -1

    assert binary_search(a, 0, len(a) - 1, 0) == 0
    assert binary_search(a, 0, len(a) - 1, 9) == 9
