import sys
input = sys.stdin.readline

N = int(input())
res = [0,0,1]

for i in range(3, N+1):
    res.append(((i-1) * (res[i-1] + res[i-2])) % 1000000000)
print(res[N])