def DP_fib(n):
    global dp
    f = [0 for i in range(n+1)]
    f[1] = 1
    f[2] = 1

    for i in range(3, n+1):
        dp += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

N = int(input())
recur = 0
dp = 0

print(DP_fib(N), dp)