import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(10001)]
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for a in range(10001):
    if arr[a] == 0:
        continue
    for j in range(arr[a]):
        sys.stdout.write(str(a) + '\n')
