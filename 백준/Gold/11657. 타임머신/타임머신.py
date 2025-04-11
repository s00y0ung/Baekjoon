import sys
input = sys.stdin.readline

def bf(start):
    distance[start] = 0

    for i in range(N):
        for j in range(1, N+1):

            if distance[j] == 1e9:
                continue

            for u,w in graph[j]:
                if distance[u] > distance[j] + w:
                    distance[u] = distance[j]+w
                    if i == N-1:
                        return True
    return False


N, M = map(int,input().split())
graph =[[] for _ in range(N+1)]
distance = [1e9 for _ in range(N+1)]

for _ in range(M):
    s,e,w = map(int, input().split())
    graph[s].append((e,w))

if bf(1):
    print(-1)
else:
    for idx in distance[2:]:
        if idx != 1e9:
            print(idx)
        else:
            print(-1)
