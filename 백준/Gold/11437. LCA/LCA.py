import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

LOG = 21  # 2 ^ 20 = 1000000

def dfs(x, depth):
    visited[x] = 1
    d[x] = depth
    for idx in graph[x]:
        if visited[idx] == 0:
            parent[idx][0] = x
            dfs(idx, depth+1)

def set_parent():
    dfs(1,0)
    for i in range(1, LOG):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if d[a] > d[b]:
        a, b = b,a

    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        return a

    for i in range(LOG-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]


N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
parent = [[0]*LOG for _ in range(N+1)]
d = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))