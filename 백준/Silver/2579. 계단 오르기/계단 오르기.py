N = int(input())
n_list = [-1]
for _ in range(N):
    n_list.append(int(input()))
dp = [0 for _ in range(N+1)]
dp[1] = n_list[1]
for i in range(2, N+1):
    dp[i] = max(dp[i-2]+n_list[i], dp[i-3]+n_list[i-1] + n_list[i])
print(dp[N])