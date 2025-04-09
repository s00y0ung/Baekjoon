import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

for k in range(N):
    for i in range(N):
        if graph[i][k] == 0:
            continue
        for j in range(N):
            if graph[i][j] == 0 and graph[k][j] != 0:
                graph[i][j] = 1
for b in graph:
    print(*[b[i] if b[i] > 0 else 0 for i in range(N)])
 