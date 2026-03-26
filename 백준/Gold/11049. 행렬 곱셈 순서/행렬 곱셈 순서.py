import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]

    for size in range(1, n):
        for start in range(n-size):
            end = start+size

            result = 1e9
            for c in range(start, end):
                result = min(result, dp[start][c]+dp[c+1][end]+m[start][0]*m[c][1]*m[end][1])
            dp[start][end] = result
    print(dp[0][-1])
if __name__ == '__main__':
    main()
