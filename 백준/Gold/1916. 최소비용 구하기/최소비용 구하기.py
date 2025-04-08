import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)

        if distance[cur] < dist:
            if end == cur:
                break
            continue

        for next in graph[cur]:
            if distance[next[0]] > dist + next[1]:
                distance[next[0]] = dist + next[1]
                heapq.heappush(q, (dist + next[1], next[0]))

N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]
distance = [1000000000] * (N+1)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
start, end = map(int, input().split())

dijkstra(start)
print(distance[end])