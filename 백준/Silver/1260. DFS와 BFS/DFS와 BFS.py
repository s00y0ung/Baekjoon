import sys
input = sys.stdin.readline

def main():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a,b = map(int, input().split())
        graph[b].append(a)
        graph[a].append(b)

    for i in range(N+1):
        graph[i].sort()
    visited = [0 for _ in range(N+1)]
    dfs(graph, V, visited)
    print()
    visited = [0 for _ in range(N + 1)]
    bfs(graph, V, visited)

def dfs(graph,V,visited):
    print(V, end = ' ')
    visited[V] = 1
    for i in graph[V]:
        if visited[i] == 0:
            dfs(graph, i, visited)

def bfs(graph, V, visited):

    que = [V]
    visited[V] = 1
    while que:
        cur = que.pop(0)
        print(cur, end = ' ')

        for i in graph[cur]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)


if __name__ == "__main__":
    main()