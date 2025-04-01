from collections import deque
import sys
input = sys.stdin.readline

def topo_sort():
    while que:
        cur = que.popleft()
        t = 0
        for b in build[cur][1:-1]:
            t = max(t, time[b])
        time[cur] = time[cur] + t

        for idx in graph[cur]:
            indegree[idx] -= 1
            if indegree[idx] == 0:
                que.append(idx)

N = int(input())

time = [0 for _ in range(N+1)]
graph =[[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
build = [[] for _ in range(N+1)]
que = deque()

for i in range(1,1+N):
    build[i] = list(map(int, input().split()))
    time[i] = build[i][0]

    for b in build[i][1:-1]:
        graph[b].append(i)
        indegree[i] += 1

for k in range(1,1+N):
    if indegree[k] == 0:
        que.append(k)

topo_sort()
time.pop(0)
print(*time, sep = '\n')