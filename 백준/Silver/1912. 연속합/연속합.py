N = int(input())
array = list(map(int, input().split()))

array_list = [0]
count = 0

for a in array:
    count += a
    array_list.append(count)

small = array_list[0]
max_sum = array_list[1]

for i in range(1, N+1):
    if small >= array_list[i-1]:
        small = array_list[i-1]

    temp = array_list[i] - small
    if max_sum < temp:
        max_sum = temp
print(max_sum)