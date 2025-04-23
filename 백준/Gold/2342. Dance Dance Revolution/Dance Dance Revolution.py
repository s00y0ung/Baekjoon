import sys
input = sys.stdin.readline

m = [[-1,2,2,2,2],[2,1,3,4,3],[2,3,1,3,4],[2,4,3,1,3],[2,3,4,3,1]]
move_list = list(map(int, input().split()))
dp = [[[1000000 for _ in range(5)] for _ in range(5)] for _ in range(len(move_list)+1)]
dp[0][0][0] = 0

s = 1
for idx in range(len(move_list)-1):
    n = move_list[idx]
    for i in range(5):
        for j in range(5):
            if i == n:
                continue
            dp[s][i][n] = min(dp[s-1][i][j] + m[j][n], dp[s][i][n])
    for i in range(5):
        for j in range(5):
            if j == n:
                continue
            dp[s][n][j] = min(dp[s-1][i][j] + m[i][n], dp[s][n][j])
    s += 1


minVal = 1000000
for i in range(5):
    for j in range(5):
        if minVal > dp[s-1][i][j]:
            minVal = dp[s-1][i][j]
print(minVal)