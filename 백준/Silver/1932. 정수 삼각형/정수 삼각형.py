import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append([-1] + list(map(int, input().split())) + [-1])
#dp = [[0 for _ in range(n+1)] for _ in range(n)]
#dp[0][1] = graph[0][1]

for h in range(1,n):
    for j in range(1,h+2):
        graph[h][j] = max(graph[h-1][j-1], graph[h-1][j]) + graph[h][j]
print(max(graph[n-1]))