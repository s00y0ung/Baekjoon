N = int(input())
arr = [*map(int, input().split())]
arr_reverse = arr[::-1]

increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[j]+1, increase[i])
        if arr_reverse[i] > arr_reverse[j]:
            decrease[i] = max(decrease[j]+1, decrease[i])
decrease = decrease[::-1]
dp = [increase[i] + decrease[i]-1 for i in range(N)]
print(max(dp))