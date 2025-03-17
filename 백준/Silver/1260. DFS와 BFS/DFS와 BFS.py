import sys
input = sys.stdin.readline

def bfs(s):
    global visited, graph
    visited[s] = 1
    queue = [s]

    while queue:
        q = queue.pop(0)
        print(q, end=" ")

        for e in graph[q]:
            if not visited[e]:
                visited[e] = 1
                queue.append(e)


def dfs(s):
    global visited, graph
    visited[s] = 1
    print(s, end=" ")

    for e in graph[s]:
        if not visited[e]:
            dfs(e)


if __name__ == "__main__":
    N, M, V = map(int, input().split())

    graph = [[]for i in range(N+1)]
    visited = [0 for i in range(N+1)]
    for i in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1, N+1):
        graph[i].sort()
    dfs(V)
    print()

    visited = [0 for i in range(N+1)]
    bfs(V)