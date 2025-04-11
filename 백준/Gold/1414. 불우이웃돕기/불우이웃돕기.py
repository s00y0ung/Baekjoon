import sys
import heapq
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def unionByRank(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
graph = []
parent = [i for i in range(N)]
ans = 0

for j in range(N):
    g = list(input().rstrip())
    for i in range(N):
        if g[i] >= 'a':
            g[i] = ord(g[i]) - 96
        elif g[i] == '0':
            g[i] = 0
        else:
            g[i] = ord(g[i]) - 38
        ans += g[i]
        heapq.heappush(graph, (g[i], i, j))

cnt = 0
while graph:
    g ,i, j = heapq.heappop(graph)
    if find(i) == find(j):
        continue
    if g == 0:
        continue

    unionByRank(i,j)
    cnt += 1
    ans -= g
    if cnt >= N-1:
        break

if cnt < N-1:
    print(-1)
else:
    print(ans)