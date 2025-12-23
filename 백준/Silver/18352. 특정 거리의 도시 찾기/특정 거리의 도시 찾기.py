import sys
input = sys.stdin.readline

def bfs(start, g, N, K):
    visited = [-1] * (N+1)
    visited[start] = 0
    que = [start]
    depth = 0
    while que:
        cur = que.pop(0)
        for c in g[cur]:
            if visited[c] == -1:
                visited[c] = visited[cur]+1
                que.append(c)
                depth = visited[c]
        if depth > K+1:
            break

    find = []
    for v in range(N+1):
        if visited[v] == K:
            find.append(v)

    if find:
        find.sort()
        for f in find:
            print(f)
    else:
        print(-1)

def main():
    N, M, K, X = map(int, input().split())
    g = [[] for _ in range(N+1)]
    for i in range(M):
        a,b = map(int, input().split())
        g[a].append(b)

    bfs(X,g,N,K)

if __name__ == "__main__":
    main()