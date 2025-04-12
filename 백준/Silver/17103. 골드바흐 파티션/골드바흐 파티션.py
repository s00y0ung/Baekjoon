import sys
input = sys.stdin.readline

N = int(input())
prime = [0 for i in range(1000001)]
for i in range(2, 1001):
    if prime[i] == 1:
        continue
    for j in range(i+i, len(prime), i):
        prime[j] = 1

for _ in range(N):
    n = int(input())

    partition = 0
    if prime[2] == 0 and prime[n-2] == 0:
        partition = 1

    s = 3
    while s <= n//2:
        if prime[s] == 0 and prime[n-s] == 0:
            partition += 1
        s += 2

    print(partition)