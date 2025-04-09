import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[1e9 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_idx = -1
min_value = 1e9

for idx in range(1, N+1):
    s = sum(graph[idx]) - graph[idx][0] - graph[idx][idx]
    if min_value > s:
        min_value = s
        min_idx = idx
        
print(min_idx)