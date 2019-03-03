def binary_search(sorted_list, value):

    beg = 0
    end = len(sorted_list)

    while beg < end:
        mid = (beg + end) // 2
        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] < value:
            beg = mid + 1
        else:
            end = mid
    return beg


def test_binary_search():
    a = list(range(10))

    assert binary_search(a, 3) == 3
    assert binary_search(a, 10) == 10
    assert binary_search(a, 9) == 9

    assert binary_search(a, 0) == 0

