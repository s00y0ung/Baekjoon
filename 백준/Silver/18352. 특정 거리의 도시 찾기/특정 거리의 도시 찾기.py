import sys
input = sys.stdin.readline

def main():
    n,m,k,x = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        g[a].append(b)
    visited = [-1]*(n+1)

    que = [x]
    visited[x] = 0
    while que:
        cur = que.pop(0)
        for i in g[cur]:
            if visited[i] == -1:
                visited[i] = visited[cur]+1
                que.append(i)
        if visited[cur] > k+1:
            break
    ans = []
    for v in range(1,n+1):
        if visited[v] == k:
            ans.append(str(v))
    if ans:
        print('\n'.join(ans))
    else:
        print(-1)
if __name__ == '__main__':
    main()