import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append([int(input()),i])
arr = sorted(arr, key = lambda x : x[0])
m = 1
for i in range(n):
    if m < arr[i][1] - i+1:
        m = arr[i][1] - i + 1
print(m)