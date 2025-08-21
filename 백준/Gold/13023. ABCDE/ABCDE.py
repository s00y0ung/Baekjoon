import sys

def backTracking(i, node, visited, depth):
    if depth == 5:
        return 1

    for k in node[i]:
        if visited[k] == 0:
            visited[k] = 1
            if backTracking(k, node, visited, depth+1):
                return 1
            visited[k] = 0
    return 0

N,M = map(int, input().split())
node = [[] for _ in range(N)]
for k in range(M):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

visited = [0 for i in range(N)]
for i in range(N):
    visited[i] = 1
    if backTracking(i, node, visited, 1):
        print(1)
        break
    visited[i] = 0
    if i == N-1:
        print(0)

