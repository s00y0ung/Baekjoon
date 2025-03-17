import sys
import copy
input = sys.stdin.readline

def bfs():
    global N, M, map, visited
    visited[0][0] = 1
    queue = [[0,0]]

    while queue:
        y,x = queue.pop(0)
        for d1,d2 in [[0,1],[0,-1],[1,0],[-1,0]]: #right, left, up, down
            ey = y + d1
            ex = x + d2
            if 0 <= ex < M and 0 <= ey < N:
                if visited[ey][ex] == 0 and map[ey][ex] == 1:
                    visited[ey][ex] = visited[y][x] + 1
                    queue.append([ey,ex])
        if visited[N-1][M-1] != 0:
            break



if __name__ == "__main__":
    N, M = map(int, input().split())
    map = [list(map(int, input().rstrip())) for i in range(N)]
    visited = [[0 for i in range(M)] for i in range(N)]

    bfs()
    print(visited[N-1][M-1])