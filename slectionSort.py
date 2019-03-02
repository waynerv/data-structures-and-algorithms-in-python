def findbiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index


def selectsort(arr):
    newarr = []
    for i in range(len(arr)):
        big = findbiggest(arr)
        newarr.append(arr.pop(big))

    return newarr


mylist = [1, 3, 5, 14, 25, 36, 46, 64, 100]
print(selectsort(mylist))
