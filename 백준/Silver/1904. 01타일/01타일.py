N = int(input())
dp = [1 for i in range(N+1)]
dp[1] = 1
for idx in range(2,N+1):
    dp[idx] = (dp[idx-2] + dp[idx-1]) % 15746
print(dp[N]%15746)