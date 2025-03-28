import sys
input = sys.stdin.readline
def bfs(x, visited, graph):
    visited[x] = 1
    que = [x]

    while que:
        n = que.pop(0)
        for node in graph[n]:
            if visited[node] == 0:
                que.append(node)
                visited[node] = visited[n] * -1
            elif visited[node] == visited[n]:
                return -1

    return 1


def solve():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for e in range(E):
        v1,v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1,V+1):
        if visited[i] == 0:
            if bfs(i, visited, graph) == -1:
                print("NO")
                return
    print("YES")


K = int(input())
for _ in range(K):
    solve()