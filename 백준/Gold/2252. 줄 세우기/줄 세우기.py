import sys
input = sys.stdin.readline
from collections import deque

def topo_sort():

    while queue:
        cur = queue.popleft()
        result.append(cur)

        for idx in graph[cur]:
            indegree[idx] -= 1
            if indegree[idx] == 0:
                queue.append(idx)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
queue = deque()
result = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for idx in range(1, len(indegree)):
    if indegree[idx] == 0:
        queue.append(idx)

topo_sort()
print(*result)