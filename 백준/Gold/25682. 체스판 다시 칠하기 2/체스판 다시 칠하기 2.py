import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [list(input().rstrip()) for _ in range(n)]
prefix = [[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(2)]
f_list = ['B','W'] * (m//2 + 1)
s_list = ['W','B'] * (m//2 + 1)
check_B = [f_list, s_list] * (n //2+1)
check_W = [s_list, f_list] * (n //2+1)

minValue = float('inf')

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[0][i][j] = prefix[0][i-1][j] + prefix[0][i][j-1] - prefix[0][i-1][j-1] + int(g[i-1][j-1] != check_B[i-1][j-1])
        prefix[1][i][j] = prefix[1][i-1][j] + prefix[1][i][j-1] - prefix[1][i-1][j-1] + int(g[i-1][j-1] != check_W[i-1][j-1])

        if i > k-1 and j > k-1:
            first = prefix[0][i][j] - prefix[0][i-k][j] - prefix[0][i][j-k] + prefix[0][i-k][j-k]
            second = prefix[1][i][j] - prefix[1][i-k][j] - prefix[1][i][j-k] + prefix[1][i-k][j-k]
            minValue = min(minValue, first, second)

print(minValue)