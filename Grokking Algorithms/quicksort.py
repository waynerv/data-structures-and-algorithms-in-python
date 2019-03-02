def quicksort(mylist):
    if len(mylist) < 2:
        return mylist
    else:
        pivot = mylist[0]
        less = [i for i in mylist[1:] if i <= pivot]
        greater = [i for i in mylist[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([2, 5, 6, 4,   23, 4545, 343, 655, 343, 42, 754]))
