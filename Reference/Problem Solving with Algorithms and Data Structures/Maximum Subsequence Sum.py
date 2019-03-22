K = int(input())
number_list = list(map(int, input().split()))
max_sum = 0
this_sum = 0
start = number_list[0]
end = number_list[-1]
temp_first_number = number_list[0]
count = 0
for i in range(K):
    if this_sum > 0:
        count += 1
    this_sum += number_list[i]
    if this_sum > max_sum:
        max_sum = this_sum
        end = number_list[i]
        start = number_list[i - count]
    elif this_sum <= 0:
        this_sum = 0
        count = 0
print(max_sum, start, end)
