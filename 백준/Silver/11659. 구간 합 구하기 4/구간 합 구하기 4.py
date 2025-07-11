import sys
n,k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

prefix = [0]
for i in range(n):
    prefix.append(prefix[-1]+num[i])
for i in range(k):
    s,e = map(int, sys.stdin.readline().split())
    print(prefix[e]-prefix[s-1])
