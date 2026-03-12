import sys
input = sys.stdin.readline

def main():
    n,e = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(e):
        a,b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    visited = [0]*(n+1)
    ans = 'YES'
    for k in range(1, n+1):
        if visited[k] == 0:
            que = [k]
            visited[k] = 1
            while que:
                cur = que.pop(0)
                for i in g[cur]:
                    if visited[i] == 0:
                        visited[i] = visited[cur]*-1
                        que.append(i)
                    elif visited[i] == visited[cur]:
                        que = []
                        ans = 'NO'
                        break
        if ans == 'NO':
            break
    print(ans)

if __name__ == '__main__':
    K = int(input())
    for _ in range(K):
        main()