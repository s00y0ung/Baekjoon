import sys
input = sys.stdin.readline

N = int(input())
prime = [False, False, True] + [True, False] * 499999
for i in range(3, 1001, 2):
    if prime[i] == False:
        continue

    for j in range(i+i, len(prime), i):
        prime[j] = False

for _ in range(N):
    n = int(input())
    partition = 0
    if prime[2] and prime[n-2]:
        partition = 1

    for s in range(3, n//2+1, 2):
        if prime[s] and prime[n-s]:
            partition += 1

    print(partition)