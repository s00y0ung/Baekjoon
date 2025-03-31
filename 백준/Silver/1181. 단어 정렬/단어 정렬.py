import sys
input = sys.stdin.readline

N = int(input().strip())

d = set()
for i in range(N):
    d.add(input().strip())

d = list(d)
d = sorted(d, key = lambda x : (len(x),x))
for i in d:
    print(i)