import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 1e9
graph =[[INF] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0
for _ in range(M):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1,N+1):
    for i in range(1, N+1):
        if graph[i][k] != 1e9:
            for j in range(1, N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


for b in graph[1:]:
    print(*[b[i] if b[i] != INF else 0 for i in range(1,1+N)])