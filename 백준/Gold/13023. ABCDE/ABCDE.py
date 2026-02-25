import sys
input = sys.stdin.readline

def backTracking(cur,visited,connect,depth):
    if depth == 5:
        return 1
    for i in connect[cur]:
        if visited[i] == 0:
            visited[i] = 1
            if backTracking(i,visited,connect, depth+1):
                return 1
            visited[i] = 0

def main():
    N,M = map(int, input().split())
    g = [[] for _ in range(N)]
    for _ in range(M):
        a,b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    visited = [0 for _ in range(N)]

    for i in range(N):
        visited[i] = 1
        if backTracking(i, visited, g, 1):
            print(1)
            return
        visited[i] = 0
    print(0)
    return
if __name__ == "__main__":
    main()