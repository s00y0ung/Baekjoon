import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)

    visited = [0 for _ in range(N+1)]
    cnt = 1
    while q:

        for _ in range(len(q)):
            n = q.popleft()
            for idx in graph[n]:
                if visited[idx] == 0:
                    visited[idx] = cnt
                    q.append(idx)
        cnt += 1
    return sum(visited) - visited[start]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_value = 1e9
min_idx = -1
for i in range(1,1+N):
    r = bfs(i)
    if min_value > r:
        min_value = r
        min_idx = i

print(min_idx)