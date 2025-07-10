def bt(k, dungeons, visited, ans):

    for i in range(len(dungeons)):
        if visited[i] or k < dungeons[i][0]:
            continue

        visited[i] = 1
        k -= dungeons[i][1]
        if ans < sum(visited):
            ans = sum(visited)
        ans = bt(k, dungeons, visited, ans)
        visited[i] = 0
        k += dungeons[i][1]

    return ans

def solution(k, dungeons):
    return bt(k, dungeons, [0 for _ in range(len(dungeons))], 0)