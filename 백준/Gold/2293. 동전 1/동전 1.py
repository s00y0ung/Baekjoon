n,k = map(int, input().split())
value = [int(input()) for i in range(n)]
value.sort()

dp = [1 if i%value[0] == 0 else 0 for i in range(k+1)]
dp[0] = 1
for i in range(1,n):
    v = value[i]
    for j in range(v, k+1):
        dp[j] = dp[j] + dp[j - v]

print(dp[k])