def bfs(maps, posi, visited):
    total = int(maps[posi[0]][posi[1]])
    visited[posi[0]][posi[1]] = 1
    que = [posi]
    while que:
        x, y = que.pop()
        for ex, ey in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            px = ex + x
            py = ey + y
            if 0 <= px < len(maps) and 0 <= py < len(maps[0]):
                if maps[px][py] == 'X' or visited[px][py] == 1:
                    continue
                total += int(maps[px][py])
                visited[px][py] = 1
                que.append((px,py))

    return visited, total


def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X' or visited[i][j] == 1:
                continue
            visited, a = bfs(maps, (i,j), visited)
            answer.append(a)
            
    answer.sort()
    if not answer:
        answer = [-1]
    return answer