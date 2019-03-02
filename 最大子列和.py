K = int(input())
number_list = list(map(int, input().split()))
max_sum = 0
this_sum = 0
for i in number_list:
    this_sum += i
    if this_sum > max_sum:
        max_sum = this_sum
    elif this_sum < 0:
        this_sum = 0
print(max_sum)
