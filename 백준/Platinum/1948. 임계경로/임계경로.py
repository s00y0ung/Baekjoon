import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = list([] for _ in range(n + 1))
reverseGraph = list([] for _ in range(n + 1))
indegree = [0] * (n + 1)

for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append([end, time])
    reverseGraph[end].append([start, time])
    indegree[end] += 1

startCity, endCity = map(int, sys.stdin.readline().split())

queue = deque()
queue.append(startCity)

result = [0] * (n + 1)

while (queue):
    now = queue.popleft()
    for next in graph[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now] + next[1])
        if (indegree[next[0]] == 0):
            queue.append(next[0])

roadCount = 0
visited = [True] * (n + 1)

queue.clear()
queue.append(endCity)
visited[endCity] = False

while (queue):
    now = queue.popleft()
    for next in reverseGraph[now]:
        if (result[next[0]] + next[1] == result[now]):
            roadCount += 1
            if (visited[next[0]]):
                visited[next[0]] = False
                queue.append(next[0])

print(result[endCity])
print(roadCount)