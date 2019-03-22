number_list = list(range(8))

def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1

assert linear_search(5, number_list) == 5