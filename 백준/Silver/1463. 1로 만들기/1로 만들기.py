import sys
input = sys.stdin.readline

N = int(input())
m = [1000000,0,1,1]

for idx in range(4, N+1):
    a = idx//2 if idx % 2 == 0 else 0
    b = idx//3 if idx % 3 == 0 else 0
    c = idx-1
    m.append(min(m[a]+1,m[b]+1,m[c]+1))
print(m[N])