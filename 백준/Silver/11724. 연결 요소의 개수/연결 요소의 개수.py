import sys
input = sys.stdin.readline

def dfs(g,cur, visited):
    s = [cur]
    visited[cur] = 1

    while s:
        cur = s.pop()
        for i in g[cur]:
            if visited[i] == 0:
                s.append(i)
                visited[i] = 1
    return visited

def main():
    N,M = map(int, input().split())
    g = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    visited = [0 for _ in range(N+1)]
    ans = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            visited = dfs(g,i,visited)
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()