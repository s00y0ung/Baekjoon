import sys
input = sys.stdin.readline

def get_e(S):
    ans = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            ans += e[S[i]][S[j]]
    return ans

def backTracking(N, start):
    global minValue
    if len(s) == N//2:
        ns = []
        for idx in range(N):
            if v[idx] == 0:
                ns.append(idx)
        m = abs(get_e(s) - get_e(ns))
        if minValue > m:
            minValue = m
        return
    for i in range(start,N):
        if v[i] == 1:
            continue
        s.append(i)
        v[i] = 1
        backTracking(N, i)
        s.remove(i)
        v[i] = 0

N = int(input())
s = [0]
v = [0 for i in range(N)]
v[0] = 1

e = [[] for _ in range(N)]
for i in range(N):
    e[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        e[i][j] = e[i][j] + e[j][i]
minValue = 1000
backTracking(N, 1)
print(minValue)