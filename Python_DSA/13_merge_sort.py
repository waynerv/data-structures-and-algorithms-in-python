import random


def merge_sort(seq):
    n = len(seq)
    if n <= 1:
        return seq
    else:
        mid = n // 2
        left_part = merge_sort(seq[:mid])
        right_part = merge_sort(seq[mid:])

        new_seq = merge_two_part(left_part, right_part)
        return new_seq


def merge_two_part(sorted_a, sorted_b):
    length_a = len(sorted_a)
    length_b = len(sorted_b)
    a = b = 0
    new_seq = list()

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_seq.append(sorted_a[a])
            a += 1
        else:
            new_seq.append(sorted_b[b])
            b += 1

    if a < length_a:
        new_seq.extend(sorted_a[a:])
    else:
        new_seq.extend(sorted_b[b:])

    return new_seq


def test_merge_sort():
    seq = list(range(10))
    random.shuffle(seq)
    new_seq = merge_sort(seq)
    assert new_seq == sorted(seq)
