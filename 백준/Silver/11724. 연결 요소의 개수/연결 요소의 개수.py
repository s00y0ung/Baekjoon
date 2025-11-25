import sys
input = sys.stdin.readline

def check(visited, k, graph):
    que = [k]
    while que:
        q = que.pop()
        for i in graph[q]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)

    return visited

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0]*(N+1)
    ans = 0
    for k in range(1, N+1):
        if visited[k] == 1:
            continue
        visited[k] = 1
        visited = check(visited, k, graph)
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()