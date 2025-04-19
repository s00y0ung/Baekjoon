import sys
input = sys.stdin.readline

s1 = [""] + list(input().rstrip())
s2 = [""] + list(input().rstrip())

g = [[""] * len(s2) for _ in range(len(s1))]

for i in range(1,len(s1)):
    for j in range(1,len(s2)):
        if s1[i] == s2[j]:
            g[i][j] = g[i-1][j-1] + s1[i]
        else:
            if len(g[i-1][j]) >= len(g[i][j-1]):
                g[i][j] = g[i-1][j]
            else:
                g[i][j] = g[i][j-1]

print(len(g[-1][-1]), g[-1][-1], sep = '\n')