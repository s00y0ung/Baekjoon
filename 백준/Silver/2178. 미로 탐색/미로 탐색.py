import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(input().strip()))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    que = [(0,0,1)]
    while que:
        curx, cury, cnt = que.pop(0)
        if curx == N-1 and cury == M-1:
            print(cnt)
            break
        for ex, ey in [(0,1), (0,-1), (-1,0), (1,0)]:
            if 0 <= curx+ex < N and 0 <= cury+ey < M:
                if graph[curx+ex][cury+ey]== '1' and visited[curx+ex][cury+ey] == 0:
                    visited[curx+ex][cury+ey] = 1
                    que.append((curx+ex, cury+ey, cnt+1))

if __name__ == "__main__":
    main()