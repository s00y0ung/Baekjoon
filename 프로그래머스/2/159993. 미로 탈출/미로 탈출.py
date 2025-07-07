def bfs(maps, s, e):
    que = [s]
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps)) ]
    visited[s[0]][s[1]] = 1
    while que:
        p = que.pop(0)
        for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            ex = x + p[0]
            ey = y + p[1]
            if 0 <= ex < len(maps) and 0 <= ey < len(maps[0]):
                if visited[ex][ey] == 1:
                    continue
                if maps[ex][ey] == 'X':
                    continue
                if maps[ex][ey] == e:
                    return [ex, ey, p[2]+1]
                que.append([ex, ey, p[2] + 1])
                visited[ex][ey] = 1
    return -1


def solution(maps):
    sx, sy = -1, -1
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = i, j
                break
    answer = bfs(maps, [sx, sy, 0], 'L')
    if answer != -1:
        r = bfs(maps,[answer[0], answer[1], 0], 'E')
        if r == -1:
            answer = -1
        else:
            answer = answer[2] + r[2]
    return answer