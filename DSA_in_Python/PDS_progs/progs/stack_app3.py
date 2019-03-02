""" 栈应用3：背包问题 """
# from stack_list import *
# from queue_list import *

########## Functions for Knap ##########

weight_list = (1, 4, 19, 14, 7, 9, 17, 29)


def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n-1], wlist, n-1):
        print("Item " + str(n) + ":", wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else:
        return False

if __name__ == "__main__":
    for w in range(6, 100, 17):
        print("Weight: ", w)
        ok = knap_rec(w, weight_list, len(weight_list))
        if not ok:
            print("No solution.")
        print("")
