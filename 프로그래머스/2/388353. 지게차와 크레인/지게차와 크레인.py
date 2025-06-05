def bfs(s, i, j, N, M):
    if i == N - 1 or j == M-1 or i == 0 or j == 0:
        return 1

    que = [(i,j)]
    visited = [[ 0 for i in range(M)] for j in range(N)]
    while que:
        i = que[0][0]
        j = que[0][1]
        del que[0]
        
        if i == N - 1 or j == M - 1 or i == 0 or j == 0:
            return 1
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if s[i + x][j + y] == '-' and visited[i+x][y+j] == 0:
                que.append((i+x,j+y))
                visited[i+x][j+y] = 1
    return -1

def solution(storage, requests):
    N = len(storage)
    M = len(storage[0])
    answer = N * M

    s = []
    for i in range(len(storage)):
        s.append(list(storage[i]))

    for request in requests:
        if len(request) == 2:
            for i in range(N):
                for j in range(M):
                    if s[i][j] == request[0]:
                        answer -= 1
                        s[i][j] = '-'
        else:
            remove = []
            for i in range(N):
                for j in range(M):
                    if s[i][j] != request:
                        continue

                    if bfs(s, i, j, N, M) == 1:
                        remove.append((i, j))

            for rx, ry in remove:
                s[rx][ry] = '-'
                answer -= 1

    return answer

