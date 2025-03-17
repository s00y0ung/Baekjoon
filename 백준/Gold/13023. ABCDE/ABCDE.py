def dfs(n, depth):
    global flag
    if depth >= 5 or flag:
        flag = 1
        return

    visited[n] = 1
    for k in graph[n]:
        if visited[k] == 0:
            dfs(k, depth+1)

    visited[n] = 0

N, M = map(int, input().split())
graph = [[] for i in range(N)]
visited = [0 for i in range(N)]
flag = 0

for i in range(M):
    f1,f2 = map(int, input().split())
    graph[f1].append(f2)
    graph[f2].append(f1)

for i in range(N):
    dfs(i, 1)
    if flag == 1:
        break;
print(flag)

