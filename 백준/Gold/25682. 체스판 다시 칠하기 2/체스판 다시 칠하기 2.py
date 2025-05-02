import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [list(input().rstrip()) for _ in range(n)]
prefix = [[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(2)]
f_list = ['B','W']
s_list = ['W','B']
minValue = 1000000000
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[0][i][j] = prefix[0][i-1][j] + prefix[0][i][j-1] - prefix[0][i-1][j-1]
        prefix[1][i][j] = prefix[1][i-1][j] + prefix[1][i][j-1] - prefix[1][i-1][j-1]

        if g[i-1][j-1] != f_list[(i+j)%2]:
            prefix[0][i][j] += 1
        if g[i-1][j-1] != s_list[(i+j)%2]:
            prefix[1][i][j] += 1

        if i > k-1 and j > k-1:
            first = abs(prefix[0][i][j] - prefix[0][i-k][j] - prefix[0][i][j-k] + prefix[0][i-k][j-k])
            second = abs(prefix[1][i][j] - prefix[1][i-k][j] - prefix[1][i][j-k] + prefix[1][i-k][j-k])
            if first < minValue:
                minValue = first
            if second < minValue:
                minValue = second

print(minValue)