import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(start):
    for n in graph[start]:
        if parent[n] != -1:
            continue
        parent[n] = start
        dfs(n)

N = int(input())
graph =[[] for _ in range(N+1)]
parent = [-1] * (N+1)
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for idx in parent[2:]:
    print(idx)