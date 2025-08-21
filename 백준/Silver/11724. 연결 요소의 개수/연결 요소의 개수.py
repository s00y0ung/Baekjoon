import sys
input = sys.stdin.readline

def check(visited, k, node):
    que = [k]

    while que:
        q = que.pop(0)
        for i in node[q]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)

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