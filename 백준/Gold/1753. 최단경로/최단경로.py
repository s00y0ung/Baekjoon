import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue

        for next in graph[cur]:
            if distance[next[0]] > dist + next[1]:
                distance[next[0]] = dist + next[1]
                heapq.heappush(q, (dist + next[1], next[0]))

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [1000000000] * (V+1)

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

dijkstra(start)
for n in distance[1:]:
    if n == 1000000000:
        print("INF")
    else:
        print(n)