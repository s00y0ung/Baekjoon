N = int(input())
d = [[0,0] for _ in range(N+1)]

d[1][0] = 0
d[1][1] = 1

for idx in range(2, N+1):
    d[idx][0] = d[idx-1][0] + d[idx-1][1]
    d[idx][1] = d[idx-1][0]
print(d[N][0] + d[N][1])