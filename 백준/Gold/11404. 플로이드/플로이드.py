import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph =[[1e9 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1,N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for idx in range(1,N+1):
    for g in graph[idx][1:]:
        if g == 1e9:
            print(0, end = " ")
        else:
            print(g, end = " ")
    print()