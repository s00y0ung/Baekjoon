import sys
input = sys.stdin.readline

N = int(input())
prime = [False, False, True] + [True, False] * 499999
p_list = []
for i in range(3, 1001, 2):
    if prime[i] == False:
        continue

    for j in range(i+i, len(prime), i):
        prime[j] = False

p_list = [i for i,x in enumerate(prime) if x]
for _ in range(N):
    n = int(input())
    partition = 0
    for p in p_list:
        e = n-p
        if e < n//2:
            break
        if prime[e]:
            partition += 1

    print(partition)