import sys
input = sys.stdin.readline

s1 = [0] + list(input().rstrip())
s2 = [0] + list(input().rstrip())
l1 = len(s1)
l2 = len(s2)

g = [[""] * l2 for _ in range(l1)]

for i in range(1,l1):
    for j in range(1,l2):
        if s1[i] == s2[j]:
            g[i][j] = g[i-1][j-1] + s1[i]
        else:
            if len(g[i-1][j]) >= len(g[i][j-1]):
                g[i][j] = g[i-1][j]
            else:
                g[i][j] = g[i][j-1]

print(len(g[-1][-1]), g[-1][-1], sep = '\n')