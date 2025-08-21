import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def check(visited, k, node):

    for i in node[k]:
        if visited[i] == 0:
            visited[i] = 1
            check(visited, i, node)

    return visited

N,M = map(int,input().split())
node = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

visited = [0 for i in range(N+1)]
ans = 0
for k in range(1,N+1):
    if visited[k] == 1:
        continue
    visited[k] = 1
    visited = check(visited, k, node)
    ans += 1

print(ans)