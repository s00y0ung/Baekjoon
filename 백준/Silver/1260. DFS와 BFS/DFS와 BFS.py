import sys
input = sys.stdin.readline

def bfs(graph, s):
    visited = [s]
    queue = [s]

    while len(queue) != 0:
        q = queue.pop(0)
        print(q, end=" ")

        for e in graph[q]:
            if e not in visited:
                visited.append(e)
                queue.append(e)


def dfs(graph, visited, s):
    visited.append(s)
    print(s, end=" ")

    for e in graph[s]:
        if e not in visited:
            dfs(graph, visited, e)


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
    dfs(graph,[], V)
    print()
    bfs(graph, V)