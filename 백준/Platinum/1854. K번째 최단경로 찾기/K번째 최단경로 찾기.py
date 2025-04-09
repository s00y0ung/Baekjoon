import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][0] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if dist > distance[cur][K-1]:
            continue

        for next in graph[cur]:
            cost = next[1] + dist
            if distance[next[0]][K-1] > cost:
                distance[next[0]][K-1] = cost
                distance[next[0]].sort()
                heapq.heappush(q, (cost, next[0]))

N, M, K = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [[INF] * K for _ in range(N+1)]

for _ in range(M):
    a,b,w = map(int, input().split())
    graph[a].append([b,w])
dijkstra(1)
for i in range(1, N+1):
    if distance[i][K-1] >= INF:
        print(-1)
    else:
        print(distance[i][K-1])