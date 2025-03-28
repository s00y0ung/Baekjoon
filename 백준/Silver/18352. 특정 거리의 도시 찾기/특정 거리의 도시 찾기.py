import sys
input = sys.stdin.readline

def bfs(x):
    global visited, graph, K
    que = [x]
    visited[x] = 0
    depth = 0

    while len(que) != 0:

        for k in range(len(que)):
            n = que.pop(0)
            for i in graph[n]:
                if visited[i] == -1:
                    que.append(i)
                    visited[i] = visited[n] + 1
                    if visited[i] > depth:
                        depth = visited[i]
        if depth > K:
            break
            
    if K not in visited:
        print(-1)
    else:
        for i in range(len(visited)):
            if visited[i] == K:
                print(i)
    return 0


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

bfs(X)