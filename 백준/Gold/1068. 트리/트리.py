import sys
input = sys.stdin.readline

def backTracking(root):
    global cnt
    if root == deleteN:
        return
    if len(graph[root]) == 0:
        cnt += 1
        return
    for n in graph[root]:
        if visited[n] == 0:
            visited[n] = 1
            backTracking(n)


N = int(input())
graph = [[] for i in range(N)]
parent = list(map(int, input().split()))
visited = [0 for i in range(N)]

deleteN = int(input())

root = []
cnt = 0
for idx in range(N):
    if parent[idx] == -1:
        root.append(idx)
        continue
    if deleteN == idx:
        continue
    p = parent[idx]
    graph[p].append(idx)

for r in root:
    backTracking(r)
print(cnt)