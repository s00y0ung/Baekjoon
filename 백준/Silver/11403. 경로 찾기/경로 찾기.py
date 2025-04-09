import sys
input = sys.stdin.readline

def dfs(root, start):

    for i in range(N):
        if visited[root][i] == 0 and graph[start][i] != 0:
            visited[root][i] = 1
            dfs(root,i)

N = int(input())
graph =[[] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
for idx in range(N):
    graph[idx] = list(map(int, input().split()))

for idx in range(N):
    dfs(idx, idx)
for b in visited:
    print(*[b[i] for i in range(N)])