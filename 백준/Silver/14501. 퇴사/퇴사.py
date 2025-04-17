N = int(input())
table = []
dp = [0 for _ in range(N+1)]
for _ in range(N):
    t, p = map(int, input().split())
    table.append([t,p])

for idx in range(N)[::-1]:
    if idx + table[idx][0] > N :
        dp[idx] = dp[idx + 1]
    else :
        dp[idx] = max(dp[idx + table[idx][0]] + table[idx][1], dp[idx + 1])

print(dp[0])