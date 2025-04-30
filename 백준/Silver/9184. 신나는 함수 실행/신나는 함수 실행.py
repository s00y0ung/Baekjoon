dp = [[[0 for _ in range(21)] for _ in range(21)]for _ in range(21)]

def dpTable():
        for a in range(21):
            for b in range(21):
                for c in range(21):
                    if a <= 0 or b <= 0 or c <= 0:
                        dp[a][b][c] = 1
                    elif a < b and b < c:
                        dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
                    else:
                        dp[a][b][c] = (
                        dp[a-1][b][c] +
                        dp[a-1][b-1][c] +
                        dp[a-1][b][c-1] -
                        dp[a-1][b-1][c-1]
                    )
        return dp
dp = dpTable()

while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = 1")
    elif a > 20 or b > 20 or c > 20:
        print(f"w({a}, {b}, {c}) = {dp[20][20][20]}")
    else:
        print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")
