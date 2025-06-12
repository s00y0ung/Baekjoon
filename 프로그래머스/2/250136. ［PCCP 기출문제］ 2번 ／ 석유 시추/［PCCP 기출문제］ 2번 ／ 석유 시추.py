def bfs(land, i, j, idx):
    que = [(i, j)]
    N = len(land[0])
    M = len(land)
    land[i][j] = idx
    cnt = 1
    while que:
        x, y = que.pop()

        for ex, ey in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 > x + ex or x + ex >= M: continue
            if 0 > y + ey or y + ey >= N: continue

            if land[ex + x][ey + y] == 1:
                que.append((ex + x, ey + y))
                land[ex + x][ey + y] = idx  # 방문 완료
                cnt += 1
    return cnt


def solution(land):
    answer = 0

    cnt_dic = {}
    idx = -1
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                c = bfs(land, i, j, idx)
                cnt_dic[idx] = c
                idx -= 1

    visited = set()
    answer = 0
    for i in range(len(land[0])):
        visited.clear()
        s = 0
        for j in range(len(land)):
            if land[j][i] < 0 and land[j][i] not in visited:
                visited.add(land[j][i])
                s += cnt_dic[land[j][i]]
        if answer < s:
            answer = s
    return answer
