import sys
input = sys.stdin.readline

def dfs(g,N,V):
    st = [V]
    visited = [0 for _ in range(N+1)]
    ans = []
    while st:
        cur = st.pop()
        if visited[cur] == 0:
            visited[cur] = 1
            ans.append(cur)
            for v in g[cur]:
                st.append(v)
    print(*ans)

def bfs(g,N,V):
    que = [V]
    visited = [0 for _ in range(N+1)]
    visited[V] = 1
    ans = []

    while que:
        cur = que.pop(0)
        ans.append(cur)
        for i in g[cur]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1
    print(*ans)

def main():
    N, M, V = map(int, input().split())
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(1,N+1):
        g[i].sort(reverse=True)
    dfs(g,N,V)
    for i in range(1,N+1):
        g[i].sort()
    bfs(g,N,V)

if __name__ == "__main__":
    main()