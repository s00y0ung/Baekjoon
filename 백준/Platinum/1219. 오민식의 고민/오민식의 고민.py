import sys
input = sys.stdin.readline

def bf(start):
    distance[start] = cost[start]

    for i in range(N):
        for j in range(N):
            if distance[j] == INF:
                continue

            for v,w in graph[j]:
                if distance[v] < distance[j] + w:
                    distance[v] = distance[j] + w
                    path[v] = j
                    if i == N-1:
                        cycle.append(v)
    if cycle:
        return True
    return False

def bfs(start):
    visited = [0 for i in range(N)]
    q = [start]
    while q:
        n = q.pop(0)
        for i in range(len(graph[n])):
            if visited[graph[n][i][0]] == 0:
                visited[graph[n][i][0]] = 1
                q.append(graph[n][i][0])
                if graph[n][i][0] == E:
                    return True
    return False

N, S, E, M = map(int, input().split())
graph = [[] for _ in range(N)]
INF = -1000000000
distance = [INF] * (N)
cycle = []
path = [-1 for _ in range(N)]

for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append([v,-1*w])
cost = list(map(int, input().split()))

for i in range(N):
    for j in range(len(graph[i])):
        graph[i][j][1] += cost[graph[i][j][0]]


if bf(S):
    if distance[E] == INF:
        print('gg')
    else:
        flag = 0
        for c in cycle:
            if bfs(c):
                print("Gee")
                flag = 1
                break
                
        if flag == 0:
            print(distance[E])
else:
    if distance[E] == INF:
        print("gg")
    else:
        print(distance[E])
