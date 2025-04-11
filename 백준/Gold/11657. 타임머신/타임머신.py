import sys
input = sys.stdin.readline

def bf(start):
    distance[start] = 0

    for i in range(N):
        for j in range(M):
            cur = graph[j][0]
            next = graph[j][1]
            weight = graph[j][2]

            if distance[cur] != 1e9 and distance[next] > distance[cur] + weight:
                distance[next] = distance[cur] + weight
                if i == N-1:
                    return True
    return False


N, M = map(int,input().split())
graph =[]
distance = [1e9 for _ in range(N+1)]

for _ in range(M):
    s,e,w = map(int, input().split())
    graph.append((s,e,w))

if bf(1):
    print(-1)
else:
    for idx in distance[2:]:
        if idx != 1e9:
            print(idx)
        else:
            print(-1)
